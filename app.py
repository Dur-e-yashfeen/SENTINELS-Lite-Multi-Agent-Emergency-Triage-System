# app.py

import os
import json
import requests
from io import BytesIO
from PIL import Image, ExifTags
import concurrent.futures
import gradio as gr
from datetime import datetime
from typing import Optional, Dict, Any

# -----------------------------
# Gemini API Client (Stub)
# -----------------------------
class GeminiClient:
    """
    Replace this stub with actual Gemini API SDK or REST integration.
    """
    def __init__(self, api_key: str):
        self.api_key = api_key

    def analyze_text(self, text: str) -> Dict[str, Any]:
        # Mock response for demo purposes
        severity = "high" if "fire" in text.lower() else "medium"
        incident_type = "fire" if "fire" in text.lower() else "unknown"
        summary = text[:200]
        return {"severity": severity, "incident_type": incident_type, "summary": summary}

    def analyze_image(self, image_bytes: bytes) -> Dict[str, Any]:
        # Mock visual cue extraction
        return {"location": {"lat": 40.7128, "lon": -74.0060}, "visual_cues": ["smoke", "fire"]}

# -----------------------------
# SENTINELS-Lite Enterprise Multi-Agent System
# -----------------------------
class SENTINELSLiteEnterprise:
    def __init__(self, api_key: str, log_file: str = "triage_log.json"):
        self.client = GeminiClient(api_key)
        self.log_file = log_file
        if not os.path.exists(self.log_file):
            with open(self.log_file, "w") as f:
                json.dump([], f)

    @staticmethod
    def filter_noise(text: str) -> str:
        return " ".join(text.strip().split())

    @staticmethod
    def download_image(image_url: str) -> Optional[bytes]:
        try:
            response = requests.get(image_url, timeout=10)
            img = Image.open(BytesIO(response.content))
            buf = BytesIO()
            img.save(buf, format="PNG")
            return buf.getvalue()
        except Exception as e:
            print(f"Image download failed: {e}")
            return None

    @staticmethod
    def extract_gps_from_image(img: Image.Image) -> Optional[Dict[str, float]]:
        try:
            exif_data = img._getexif()
            if not exif_data:
                return None
            gps_info = {ExifTags.TAGS.get(k): v for k, v in exif_data.items() if k in ExifTags.TAGS}
            if "GPSInfo" in gps_info:
                gps = gps_info["GPSInfo"]
                lat = gps.get(2)
                lon = gps.get(4)
                if lat and lon:
                    return {"lat": lat[0]/lat[1], "lon": lon[0]/lon[1]}
            return None
        except Exception:
            return None

    def log_incident(self, record: Dict[str, Any]):
        """Append triage record to log file for analytics."""
        with open(self.log_file, "r+") as f:
            data = json.load(f)
            record["logged_at"] = datetime.utcnow().isoformat() + "Z"
            data.append(record)
            f.seek(0)
            json.dump(data, f, indent=2)

    def triage_incident(self, text: str, image_url: Optional[str] = None) -> Dict[str, Any]:
        clean_text = self.filter_noise(text)
        image_bytes = self.download_image(image_url) if image_url else None

        results = {}
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = {}
            futures["text"] = executor.submit(self.client.analyze_text, clean_text)
            if image_bytes:
                futures["image"] = executor.submit(self.client.analyze_image, image_bytes)
            for key, future in futures.items():
                try:
                    results[key] = future.result()
                except Exception as e:
                    results[key] = {"error": str(e)}

        # Combine results
        severity = results.get("text", {}).get("severity", "unknown")
        incident_type = results.get("text", {}).get("incident_type", "unknown")
        summary = results.get("text", {}).get("summary", clean_text[:200])
        location = results.get("image", {}).get("location") or {"lat": 0.0, "lon": 0.0}
        visual_cues = results.get("image", {}).get("visual_cues", [])

        record = {
            "severity": severity,
            "incident_type": incident_type,
            "location": location,
            "summary": summary,
            "visual_cues": visual_cues,
            "structured_data": results
        }

        # Log the incident
        self.log_incident(record)
        return record

# -----------------------------
# Gradio Interface
# -----------------------------
def triage_endpoint(api_key: str, text: str, image_url: str = ""):
    if not api_key:
        return {"error": "API key is required."}
    agent = SENTINELSLiteEnterprise(api_key)
    result = agent.triage_incident(text, image_url.strip() or None)
    return json.dumps(result, indent=2)

with gr.Blocks() as demo:
    gr.Markdown("## SENTINELS-Lite Enterprise Emergency Triage System")
    api_key_input = gr.Textbox(label="Gemini API Key", type="password")
    text_input = gr.Textbox(label="Incident Description (Text)")
    image_input = gr.Textbox(label="Incident Image URL (Optional)")
    output_box = gr.Code(label="Triage JSON Output", language="json")
    submit_btn = gr.Button("Generate Triage Record")
    
    submit_btn.click(
        triage_endpoint,
        inputs=[api_key_input, text_input, image_input],
        outputs=[output_box]
    )

if __name__ == "__main__":
    demo.launch()