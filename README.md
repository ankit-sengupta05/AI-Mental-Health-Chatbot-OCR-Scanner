<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00e5c8,50:6c63ff,100:ff4d8d&height=200&section=header&text=MindScan%20AI&fontSize=60&fontColor=ffffff&fontAlignY=38&desc=Mental%20Health%20Chatbot%20%2B%20Medical%20OCR%20Scanner&descAlignY=58&descSize=18&animation=fadeIn" width="100%"/>

<br/>

<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=20&pause=1000&color=00E5C8&center=true&vCenter=true&width=750&lines=🧠+Emotion+Intelligence+%2B+Medical+OCR+Pipeline;⚡+DistilRoBERTa+%7C+Pytesseract+%7C+Flask+REST+API;🔬+7-Class+NLP+Emotion+Classification;📄+Real-Time+Medical+Report+Parsing;🔗+Cross-Reference+Engine+%C3%97+Mental+Health+AI" alt="Typing SVG" />
</a>

<br/><br/>

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=for-the-badge&logo=flask&logoColor=white)
![HuggingFace](https://img.shields.io/badge/🤗_Transformers-4.x-FFD21E?style=for-the-badge)
![Tesseract](https://img.shields.io/badge/Tesseract-OCR-4285F4?style=for-the-badge&logo=google&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-00e5c8?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)
![Flake8](https://img.shields.io/badge/Flake8-Passing-6c63ff?style=for-the-badge&logo=python&logoColor=white)
![PRs](https://img.shields.io/badge/PRs-Welcome-ff4d8d?style=for-the-badge&logo=github&logoColor=white)

<br/>

> **Emotion intelligence meets medical data** — real-time NLP sentiment analysis powered by `DistilRoBERTa` + structured medical report extraction via `Pytesseract OCR` + intelligent cross-referencing against a curated conditions database.

</div>

---

## 📡 System Architecture

```
╔═════════════════════════════════════════════════════════════════════════╗
║                        🧠  MindScan AI  System                         ║
╠═══════════════════════╦═════════════════════════╦═══════════════════════╣
║   💬 NLP ENGINE       ║   📄 OCR PIPELINE       ║   🔗 CROSS-REF        ║
║                       ║                         ║                       ║
║  Text Input           ║  Image Upload           ║  Emotion Data  +      ║
║       ↓               ║        ↓                ║  OCR Report           ║
║  DistilRoBERTa        ║  Pytesseract OCR        ║       ↓               ║
║  (7-class emotions)   ║  + PIL Grayscale        ║  medical_keywords     ║
║       ↓               ║        ↓                ║  .json DB Lookup      ║
║  Confidence Score     ║  Regex Parser           ║       ↓               ║
║  + Risk Level         ║  (vitals/labs/meds)     ║  Correlation Note     ║
║       ↓               ║        ↓                ║  + Matched Conditions ║
║  Advice Generator     ║  Structured JSON        ║                       ║
╚═══════════════════════╩═════════════════════════╩═══════════════════════╝
                                    ↓
                  ┌─────────────────────────────────────┐
                  │   🐍  Flask REST API  (port 5000)   │
                  └─────────────────────────────────────┘
                                    ↓
                  ┌─────────────────────────────────────┐
                  │   🌐  Vanilla JS Dark-Mode Frontend  │
                  └─────────────────────────────────────┘
```

---

## ✨ Feature Matrix

| Feature | Technology | Details | Status |
|:--------|:-----------|:--------|:------:|
| 💬 **7-Class Emotion Classification** | `distilroberta-base` | joy · sadness · anger · fear · disgust · surprise · neutral | ✅ |
| 📊 **Confidence Scoring + Risk Levels** | Custom `EMOTION_MENTAL_MAP` | low / low-medium / medium / high | ✅ |
| 🏥 **Medical Image OCR** | `pytesseract` + `Pillow` | Grayscale preprocessing + PSM 6 config | ✅ |
| 🧪 **Lab Value Extraction** | Regex pipeline | HbA1c · Glucose · WBC · RBC · TSH · T3 · T4 | ✅ |
| ❤️ **Vitals Detection** | Regex pipeline | BP · HR · SpO2 · BMI · Temp · Weight | ✅ |
| 💊 **Medication Parsing** | Dosage pattern matching | mg · mcg · ml dosage detection | ✅ |
| 🔗 **Emotion × Medical Cross-Ref** | `medical_keywords.json` + rule engine | Condition–emotion correlation | ✅ |
| 🌐 **Dark Mode SPA Frontend** | Vanilla HTML/CSS/JS | Drag & drop · emotion bars · typing indicator | ✅ |
| 🔒 **Pre-commit Security Hooks** | flake8 + codespell + secret scan | PEP8 enforced · secrets blocked | ✅ |

---

## 🧠 Emotion Classification Engine

**Model:** `j-hartmann/emotion-english-distilroberta-base` · 124M parameters · fine-tuned on 6 emotion datasets

| Emotion | Risk Level | Color | Clinical Advice |
|:-------:|:----------:|:-----:|:----------------|
| 😊 `joy` | 🟢 `low` | `green` | Maintain healthy routines and positive habits |
| 😢 `sadness` | 🟡 `medium` | `blue` | Reach out to a friend or licensed therapist |
| 😠 `anger` | 🟡 `medium` | `orange` | Deep breathing, journaling, and cool-down techniques |
| 😨 `fear` | 🔴 `high` | `red` | Grounding techniques + professional support advised |
| 😒 `disgust` | 🟠 `low-medium` | `yellow` | Reflect on boundary violations · consider counseling |
| 😲 `surprise` | 🟢 `low` | `teal` | Allow time to process unexpected events |
| 😐 `neutral` | 🟢 `low` | `gray` | Stay consistent with self-care practices |

> [!NOTE]
> The `UNEXPECTED` key warning for `roberta.embeddings.position_ids` at model load time is **harmless**.
> It is a known artifact when loading RoBERTa checkpoints across different task heads and can be safely ignored.

---

## 📁 Project Structure

```
AI-Mental-Health-Chatbot-OCR-Scanner/
│
├── 🐍 backend/
│   ├── app.py                  ←  Flask API server · routes + CORS
│   ├── sentiment_model.py      ←  DistilRoBERTa emotion classifier
│   ├── ocr_pipeline.py         ←  Pytesseract OCR + regex report parser
│   ├── medical_crossref.py     ←  Emotion × medical DB cross-referencer
│   └── requirements.txt        ←  Python dependencies
│
├── 📦 data/
│   └── medical_keywords.json   ←  Curated conditions · symptoms · meds DB
│
├── 🌐 frontend/
│   └── index.html              ←  Single-page dark UI (vanilla JS)
│
├── ⚙️  scripts/                ←  Helper / setup scripts
├── 🔧 .github/                 ←  GitHub Actions CI workflows
├── 🪝 .pre-commit-config.yaml  ←  flake8 + secret scan + codespell hooks
└── 📋 requirements.txt         ←  Root-level requirements
```

---

## 🚀 Quick Start

### 1️⃣  Prerequisites

> Tesseract OCR must be installed on your system PATH before running:

| Platform | Install Command |
|:--------:|:----------------|
| 🪟 **Windows** | Download installer from [UB-Mannheim](https://github.com/UB-Mannheim/tesseract/wiki) → add to system PATH |
| 🍎 **macOS** | `brew install tesseract` |
| 🐧 **Linux** | `sudo apt install tesseract-ocr` |

### 2️⃣  Clone & Install

```bash
# Clone the repository
git clone https://github.com/your-username/AI-Mental-Health-Chatbot-OCR-Scanner.git
cd AI-Mental-Health-Chatbot-OCR-Scanner

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate          # Windows
source venv/bin/activate       # macOS / Linux

# Install Python dependencies
cd backend
pip install -r requirements.txt
```

### 3️⃣  Launch Backend

```bash
python app.py
```

```
Loading weights: 100%|████████████████████| 105/105
RobertaForSequenceClassification loaded from j-hartmann/emotion-english-distilroberta-base
 * Running on http://127.0.0.1:5000
 * Debug mode: on ✅
```

### 4️⃣  Open Frontend

```bash
# Serve from project root
python -m http.server 8080 --directory frontend
# → Open http://localhost:8080
```

---

## 🔌 API Reference

> **Base URL:** `http://localhost:5000/api`  ·  All responses return `Content-Type: application/json`

---

### 🟢 `POST`  `/api/chat`

> Analyze free-text input for emotional state using DistilRoBERTa NLP

```http
POST /api/chat
Content-Type: application/json
```

**Request Body**

```json
{
  "message": "I've been feeling really anxious and overwhelmed lately."
}
```

**Response · `200 OK`**

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
      { "label": "fear",    "score": 78.4 },
      { "label": "sadness", "score": 12.1 },
      { "label": "neutral", "score": 5.3  },
      { "label": "anger",   "score": 2.8  }
    ]
  }
}
```

| Field | Type | Description |
|:------|:----:|:------------|
| `dominant_emotion` | `string` | Highest-confidence emotion label |
| `confidence` | `float` | Score 0–100 for dominant emotion |
| `risk_level` | `string` | `low` · `low-medium` · `medium` · `high` |
| `color` | `string` | UI color token for the emotion |
| `advice` | `string` | Personalized mental health guidance |
| `all_emotions` | `array` | Full sorted probability distribution |

---

### 🟣 `POST`  `/api/ocr`

> Upload a medical report image — extracts vitals, lab values, medications, and diagnoses via OCR

```http
POST /api/ocr
Content-Type: multipart/form-data
```

**Request Form Data**

```
file: <image/png | image/jpeg | image/tiff>
```

**Response · `200 OK`**

```json
{
  "status": "success",
  "ocr_result": {
    "patient_name": "John Doe",
    "date": "10/03/2026",
    "vitals": {
      "BP": "120/80",
      "HR": "72 bpm",
      "SpO2": "98%",
      "BMI": "22.4"
    },
    "lab_values": {
      "Glucose":     "95 mg/dL",
      "HbA1c":       "5.4%",
      "Cholesterol": "182 mg/dL",
      "Hemoglobin":  "13.8 g/dL"
    },
    "diagnoses":   ["Impression: Generalized Anxiety Disorder"],
    "medications": ["Sertraline 50mg daily", "Clonazepam 0.5mg"],
    "raw_text": "..."
  }
}
```

| Field | Type | Extraction Method |
|:------|:----:|:------------------|
| `patient_name` | `string\|null` | Heuristic: `Patient:` / `Name:` label |
| `date` | `string\|null` | Regex: `DD/MM/YYYY` or `MM-DD-YY` |
| `vitals` | `object` | Regex: BP · HR · Temp · SpO2 · BMI · Weight |
| `lab_values` | `object` | Regex: HbA1c · Glucose · WBC · RBC · TSH · T3/T4 |
| `medications` | `array` | Lines containing `mg` / `mcg` / `ml` |
| `diagnoses` | `array` | Lines with diagnosis / impression / assessment |

---

### 🟠 `POST`  `/api/analyze`

> **Combined endpoint** — runs emotion NLP + OCR extraction + cross-reference in a single call

```http
POST /api/analyze
Content-Type: multipart/form-data
```

**Request Form Data**

```
message: "I feel exhausted and completely hopeless"    (optional)
file:    <medical report image>                        (optional)
```

**Response · `200 OK`**

```json
{
  "status": "success",
  "emotion_analysis": { "...": "..." },
  "ocr_result": { "...": "..." },
  "cross_reference": {
    "condition_matches": [
      {
        "condition": "depression",
        "matched_symptoms": ["hopelessness", "fatigue", "low energy"],
        "known_medications": ["Sertraline", "Fluoxetine", "Bupropion"],
        "recommendation": "Consult a psychiatrist for a full evaluation."
      }
    ],
    "emotion_health_correlation": "⚠️ Your emotional state aligns with detected medical indicators. Professional consultation is strongly advised.",
    "total_matches": 1
  }
}
```

---

### 🔵 `GET`  `/api/health`

> Service liveness check — use to verify the backend is running

```http
GET /api/health
```

**Response · `200 OK`**

```json
{
  "status": "ok",
  "service": "Mental Health AI API"
}
```

---

## 📦 Full Tech Stack

| Layer | Library / Tool | Version | Purpose |
|:------|:--------------|:-------:|:--------|
| 🧠 **NLP Model** | `distilroberta-base` (HuggingFace) | — | Emotion classification inference |
| 🐍 **Web Framework** | `Flask` | 2.x | REST API server |
| 🔗 **CORS** | `flask-cors` | latest | Cross-origin header management |
| 🖼️ **OCR Engine** | `pytesseract` | latest | Image → raw text extraction |
| 🖼️ **Image Processing** | `Pillow` (PIL) | latest | Grayscale preprocessing |
| 📡 **ML Pipeline** | `transformers` (HuggingFace) | 4.x | Model loading + inference |
| 🌐 **Frontend** | Vanilla HTML / CSS / JS | — | SPA dark-mode UI |
| 🔒 **Code Quality** | `flake8` + `pre-commit` | — | PEP8 linting + secret scanning |

---

## 🪝 Pre-commit Hook Status

```
detect private key ...................... ✅  Passed
don't commit to branch .................. ✅  Passed
flake8 .................................. ✅  Passed   ← E302 · E501 · E741 all resolved
codespell ............................... ✅  Passed
mask secrets in staged files ............ ✅  Passed
syntax and compile check ................ ✅  Passed
```

---

## ⚠️ Medical Disclaimer

> [!CAUTION]
> This tool is intended for **educational and research purposes only**.
> It is **not a substitute** for professional medical or psychological advice, diagnosis, or treatment.
> If you or someone you know is experiencing a mental health crisis, please contact a qualified healthcare professional or a crisis helpline **immediately**.

---

## 🤝 Contributing

```bash
# 1. Fork the repo and create your branch
git checkout -b feature/amazing-feature

# 2. Commit your changes with a descriptive message
git commit -m "feat: add amazing feature"

# 3. Push to your fork and open a Pull Request
git push origin feature/amazing-feature
```

> Run `pre-commit install` after cloning to enable all local hooks.

---

## 📄 License

<div align="center">

This project is licensed under the **MIT License**

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:ff4d8d,50:6c63ff,100:00e5c8&height=120&section=footer" width="100%"/>

</div>
