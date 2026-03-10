# 🧠 MindScan AI — Mental Health Chatbot + OCR Scanner

> Emotion intelligence meets medical data — real-time sentiment analysis powered by DistilRoBERTa + medical report parsing via Pytesseract OCR.

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=flat&logo=flask&logoColor=white)
![HuggingFace](https://img.shields.io/badge/HuggingFace-Transformers-FFD21E?style=flat&logo=huggingface&logoColor=black)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)

---

## ✨ Features

- **💬 Emotion Intelligence Engine** — Classifies 7 emotions (joy, sadness, anger, fear, disgust, surprise, neutral) from free-text input using the `j-hartmann/emotion-english-distilroberta-base` model
- **📄 Medical Report Scanner** — Uploads prescription/lab images, runs Pytesseract OCR, and extracts structured fields (vitals, lab values, medications, diagnoses)
- **🔗 Cross-Reference Engine** — Correlates detected emotions with medical report findings using a curated `medical_keywords.json` dataset
- **⚡ REST API** — Clean Flask endpoints for chat analysis, OCR scanning, and combined full analysis
- **🌐 Modern Frontend** — Single-page dark-mode UI with real-time emotion bars, animated typing indicators, and drag-and-drop file upload

---

## 📁 Project Structure

```
AI-Mental-Health-Chatbot-OCR-Scanner/
├── backend/
│   ├── app.py                  # Flask API server (routes + CORS)
│   ├── sentiment_model.py      # DistilRoBERTa emotion classifier
│   ├── ocr_pipeline.py         # Pytesseract OCR + report parser
│   ├── medical_crossref.py     # Emotion × medical data cross-referencer
│   └── requirements.txt        # Python dependencies
├── data/
│   └── medical_keywords.json   # Curated conditions, symptoms & medications DB
├── frontend/
│   └── index.html              # Single-page UI (vanilla HTML/CSS/JS)
├── scripts/                    # Helper/setup scripts
├── .github/                    # GitHub Actions workflows
├── .gitignore
├── .pre-commit-config.yaml
└── requirements.txt            # Root-level requirements
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) installed on your system
  - **Windows:** Download from [UB-Mannheim](https://github.com/UB-Mannheim/tesseract/wiki) and add to PATH
  - **macOS:** `brew install tesseract`
  - **Linux:** `sudo apt install tesseract-ocr`

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/AI-Mental-Health-Chatbot-OCR-Scanner.git
   cd AI-Mental-Health-Chatbot-OCR-Scanner
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

4. **Run the Flask backend**
   ```bash
   python app.py
   ```
   The server will start at `http://127.0.0.1:5000`. On first run, the DistilRoBERTa model weights (~300MB) will be downloaded automatically from HuggingFace.

5. **Open the frontend**

   Open `frontend/index.html` directly in your browser, or serve it with any static server:
   ```bash
   # Python simple server from project root
   python -m http.server 8080 --directory frontend
   ```
   Then visit `http://localhost:8080`.

---

## 🔌 API Reference

All endpoints are served from `http://localhost:5000/api`.

### `POST /api/chat`
Analyze a message for emotional state.

**Request body:**
```json
{ "message": "I've been feeling really anxious and overwhelmed lately." }
```

**Response:**
```json
{
  "status": "success",
  "emotion_analysis": {
    "dominant_emotion": "fear",
    "confidence": 78.4,
    "risk_level": "high",
    "color": "red",
    "advice": "Fear and anxiety are linked. Grounding techniques and professional support are recommended.",
    "all_emotions": [
      { "label": "fear", "score": 78.4 },
      { "label": "sadness", "score": 12.1 },
      ...
    ]
  }
}
```

### `POST /api/ocr`
Upload a medical report image for OCR extraction.

**Request:** `multipart/form-data` with field `file` (PNG, JPG, TIFF)

**Response:**
```json
{
  "status": "success",
  "ocr_result": {
    "patient_name": "John Doe",
    "date": "10/03/2026",
    "vitals": { "BP": "120/80", "HR": "72 bpm" },
    "lab_values": { "Glucose": "95 mg/dL" },
    "diagnoses": ["Impression: Generalized Anxiety Disorder"],
    "medications": ["Sertraline 50mg daily"],
    "raw_text": "..."
  }
}
```

### `POST /api/analyze`
Combined emotion + OCR + cross-reference analysis.

**Request:** `multipart/form-data` with optional `message` (text) and `file` (image)

### `GET /api/health`
Health check endpoint. Returns `{ "status": "ok" }`.

---

## 🧠 Model Details

| Component | Model / Library | Purpose |
|-----------|----------------|---------|
| Emotion NLP | `j-hartmann/emotion-english-distilroberta-base` | 7-class emotion classification |
| OCR | `pytesseract` + `Pillow` | Text extraction from medical images |
| Cross-reference | Custom JSON + rule engine | Condition–emotion correlation |

The `UNEXPECTED` key warning for `roberta.embeddings.position_ids` during model load is harmless — it's a known artifact when loading RoBERTa checkpoints across different task heads and can be safely ignored.

---

## ⚠️ Disclaimer

This tool is intended for **educational and research purposes only**. It is **not a substitute for professional medical or psychological advice, diagnosis, or treatment**. If you are experiencing a mental health crisis, please contact a qualified healthcare professional or a crisis helpline immediately.

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

Pre-commit hooks are configured via `.pre-commit-config.yaml`. Run `pre-commit install` after cloning to enable them.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
