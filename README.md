# SENTINELS-Lite: Multi-Agent Emergency Triage System

**SENTINELS-Lite** is an AI-powered emergency response platform that converts raw multi-modal incident reports (text + images) into actionable triage records. It is designed for rapid, accurate emergency dispatch and decision-making. This project was developed as part of an **Enterprise Agent Capstone Project**.

---

## Features

- **Multi-Agent System:** Parallel processing of text and images for faster triage.
- **LLM Integration:** Uses Gemini API to classify severity, extract structured data, and generate summaries.
- **Multi-Modal Input:** Accepts text descriptions and image URLs.
- **Structured JSON Output:** Provides actionable records ready for emergency dispatch.
- **Logging & Analytics:** Logs incidents with timestamps for KPI tracking.
- **Deployable Interface:** Simple Gradio UI for testing and deployment.

---

## Pipeline Overview

1. **Noise Filtering:** Cleans the text input for better LLM processing.
2. **Image Analysis (Optional):** Detects visual cues like fire, smoke, or accidents.
3. **Severity Classification & Structured Extraction:** Parallel agents analyze text and image inputs.
4. **JSON Triage Record Generation:** Combines results into a standardized triage record.
5. **Logging:** Records each incident for monitoring and analytics.

Here’s a **professional, submission-ready `README.md`** for your GitHub repository with SENTINELS-Lite:

```markdown
# SENTINELS-Lite: Multi-Agent Emergency Triage System

**SENTINELS-Lite** is an AI-powered emergency response platform that converts raw multi-modal incident reports (text + images) into actionable triage records. It is designed for rapid, accurate emergency dispatch and decision-making. This project was developed as part of an **Enterprise Agent Capstone Project**.

---

## Features

- **Multi-Agent System:** Parallel processing of text and images for faster triage.
- **LLM Integration:** Uses Gemini API to classify severity, extract structured data, and generate summaries.
- **Multi-Modal Input:** Accepts text descriptions and image URLs.
- **Structured JSON Output:** Provides actionable records ready for emergency dispatch.
- **Logging & Analytics:** Logs incidents with timestamps for KPI tracking.
- **Deployable Interface:** Simple Gradio UI for testing and deployment.

---

## Pipeline Overview

1. **Noise Filtering:** Cleans the text input for better LLM processing.
2. **Image Analysis (Optional):** Detects visual cues like fire, smoke, or accidents.
3. **Severity Classification & Structured Extraction:** Parallel agents analyze text and image inputs.
4. **JSON Triage Record Generation:** Combines results into a standardized triage record.
5. **Logging:** Records each incident for monitoring and analytics.

---

## Example Incident Input

**Text Description:**
```

Fire broke out on the 5th floor of a commercial building at 123 Main Street. Smoke is visible, and people are evacuating. Immediate fire department response needed.

```

**Sample Output (JSON):**
```json
{
  "severity": "high",
  "incident_type": "fire",
  "location": {"lat": 40.7128, "lon": -74.0060},
  "summary": "Fire reported at building on 5th Avenue...",
  "visual_cues": ["smoke", "fire"],
  "structured_data": {
    "text": {...},
    "image": {...}
  },
  "logged_at": "2025-12-01T19:30:00Z"
}
````

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/sentinels-lite.git
cd sentinels-lite
```

2. Install dependencies:

```bash
pip install gradio pillow requests
```

---

## Usage

Run the application locally:

```bash
python app.py
```

1. Open the Gradio UI in your browser (`http://localhost:7860`).
2. Enter your **Gemini API key**, the incident description, and optional image URL.
3. Click **Generate Triage Record** to receive structured JSON output.

---

## Logging & Analytics

All processed incidents are logged in `triage_log.json` with timestamps. This enables KPI tracking and further analysis of emergency trends.

---

## Contributing

Contributions are welcome! Please submit pull requests with clear descriptions and maintain code formatting standards.

---

## License

This project is released under the MIT License.

---

## Contact

For questions or inquiries, contact **dureyashfeen/ dureyashfeen**.

```


