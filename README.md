<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00e5c8,50:6c63ff,100:ff4d8d&height=210&section=header&text=MindScan%20AI&fontSize=65&fontColor=ffffff&fontAlignY=38&desc=Mental%20Health%20Chatbot%20%2B%20Medical%20OCR%20Scanner&descAlignY=58&descSize=18&animation=fadeIn" width="100%"/>

<br/>

<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=700&size=20&pause=1000&color=00E5C8&center=true&vCenter=true&width=800&lines=🧠+AI-Powered+Mental+Health+NLP+%2B+OCR+Pipeline;⚡+DistilRoBERTa+%7C+Flask+REST+API+%7C+Pytesseract;🔬+7-Class+Real-Time+Emotion+Classification;📄+Intelligent+Medical+Report+Parsing+%26+Extraction;🔗+Emotion+%C3%97+Medical+Data+Cross-Reference+Engine" alt="Typing SVG" />
</a>

<br/><br/>

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-REST_API-000000?style=for-the-badge&logo=flask&logoColor=white)
![HuggingFace](https://img.shields.io/badge/🤗_HuggingFace-Transformers_4.x-FFD21E?style=for-the-badge)
![Tesseract](https://img.shields.io/badge/Tesseract-OCR_Engine-4285F4?style=for-the-badge&logo=google&logoColor=white)
![Pillow](https://img.shields.io/badge/Pillow-Image_Processing-11A0D9?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-00e5c8?style=for-the-badge)
![Status](https://img.shields.io/badge/Build-Passing-brightgreen?style=for-the-badge&logo=githubactions&logoColor=white)
![Flake8](https://img.shields.io/badge/Flake8-PEP8_Clean-6c63ff?style=for-the-badge&logo=python&logoColor=white)
![PRs](https://img.shields.io/badge/PRs-Welcome-ff4d8d?style=for-the-badge&logo=github&logoColor=white)

<br/>

> **🧠 Emotion intelligence meets clinical data** — production-ready NLP sentiment analysis pipeline powered by `DistilRoBERTa` + structured medical report extraction via `Pytesseract OCR` + intelligent cross-referencing against a curated medical conditions database — served through a blazing-fast **Flask REST API**.

</div>

---

## 📡 System Architecture

```
╔══════════════════════════════════════════════════════════════════════════╗
║                        🧠  MindScan AI  System                          ║
╠════════════════════════╦══════════════════════════╦═══════════════════════╣
║   💬 NLP ENGINE        ║   📄 OCR PIPELINE        ║   🔗 CROSS-REF        ║
║                        ║                          ║                       ║
║  User Text Input       ║  Medical Image Upload    ║  Emotion JSON  +      ║
║        ↓               ║          ↓               ║  OCR Report JSON      ║
║  DistilRoBERTa         ║  Pytesseract + PIL       ║          ↓            ║
║  (7-class emotions)    ║  Grayscale → PSM 6       ║  medical_keywords     ║
║        ↓               ║          ↓               ║  .json  DB  Lookup    ║
║  Confidence Score      ║  Regex Parser            ║          ↓            ║
║  + Risk Assessment     ║  vitals · labs · meds    ║  Correlation Engine   ║
║        ↓               ║          ↓               ║  + Matched Conditions ║
║  Personalised Advice   ║  Structured JSON Output  ║                       ║
╚════════════════════════╩══════════════════════════╩═══════════════════════╝
                                     ↓
               ┌──────────────────────────────────────────┐
               │   🐍  Flask REST API  ·  port 5000        │
               │   CORS-enabled  ·  JSON responses         │
               └──────────────────────────────────────────┘
                                     ↓
               ┌──────────────────────────────────────────┐
               │   🌐  Vanilla JS SPA  ·  Dark Mode UI     │
               │   Drag & Drop  ·  Emotion Bars  ·  OCR   │
               └──────────────────────────────────────────┘
```

---

## ✨ Feature Matrix

| Feature | Technology | Details | Status |
|:--------|:-----------|:--------|:------:|
| 💬 **7-Class Emotion NLP** | `distilroberta-base` | joy · sadness · anger · fear · disgust · surprise · neutral | ✅ Live |
| 📊 **Confidence Scoring + Risk Levels** | `EMOTION_MENTAL_MAP` ruleset | low · low-medium · medium · high | ✅ Live |
| 🏥 **Medical Image OCR** | `pytesseract` + `Pillow` | Grayscale enhance · PSM 6 config | ✅ Live |
| 🧪 **Lab Value Extraction** | Regex NLP pipeline | HbA1c · Glucose · WBC · RBC · TSH · T3 · T4 | ✅ Live |
| ❤️ **Vitals Detection** | Regex pattern matching | BP · HR · SpO2 · BMI · Temp · Weight | ✅ Live |
| 💊 **Medication Parsing** | Dosage unit detection | mg · mcg · ml lines extracted | ✅ Live |
| 🔗 **Emotion × Medical Cross-Ref** | JSON rule engine | Condition–emotion clinical correlation | ✅ Live |
| 🌐 **Dark Mode SPA** | Vanilla HTML/CSS/JS | Drag & drop · animated bars · typing UX | ✅ Live |
| 🔒 **Pre-commit Security Pipeline** | flake8 + codespell + secret scan | PEP8 enforced · secrets blocked | ✅ Live |

---

## 🧠 Emotion Classification Engine

> **Model:** `j-hartmann/emotion-english-distilroberta-base` · 124M parameters · fine-tuned across 6 emotion datasets

| Emotion | Risk Level | Color Token | Clinical Recommendation |
|:-------:|:----------:|:-----------:|:------------------------|
| 😊 `joy` | 🟢 `low` | `green` | Reinforce positive behavioural routines |
| 😢 `sadness` | 🟡 `medium` | `blue` | Encourage therapeutic support & social connection |
| 😠 `anger` | 🟡 `medium` | `orange` | Deep breathing · CBT journaling · cool-down protocol |
| 😨 `fear` | 🔴 `high` | `red` | Grounding techniques · immediate professional referral |
| 😒 `disgust` | 🟠 `low-medium` | `yellow` | Boundary reflection · counselling recommended |
| 😲 `surprise` | 🟢 `low` | `teal` | Allow cognitive processing time for new stimuli |
| 😐 `neutral` | 🟢 `low` | `gray` | Maintain consistent self-care & wellness practices |

> [!NOTE]
> The `UNEXPECTED` key warning for `roberta.embeddings.position_ids` at model load is **harmless** — known cross-architecture artifact, safely ignored.

---

## 📁 Project Structure

```
AI-Mental-Health-Chatbot-OCR-Scanner/
│
├── 🐍 backend/
│   ├── app.py                  ←  Flask REST API server · routes + CORS
│   ├── sentiment_model.py      ←  DistilRoBERTa NLP emotion classifier
│   ├── ocr_pipeline.py         ←  Pytesseract OCR + regex report parser
│   ├── medical_crossref.py     ←  Emotion × medical DB cross-referencer
│   └── requirements.txt        ←  Pinned Python dependencies
│
├── 📦 data/
│   └── medical_keywords.json   ←  Curated conditions · symptoms · medications DB
│
├── 🌐 frontend/
│   └── index.html              ←  SPA dark-mode UI · vanilla JS
│
├── ⚙️  scripts/                ←  Automation + helper scripts
├── 🔧 .github/                 ←  GitHub Actions CI/CD workflows
├── 🪝 .pre-commit-config.yaml  ←  flake8 · secret scan · codespell hooks
└── 📋 requirements.txt         ←  Root-level requirements
```

---

## 🚀 Quick Start

### 1️⃣ Prerequisites

| Platform | Install Tesseract OCR |
|:--------:|:----------------------|
| 🪟 **Windows** | [UB-Mannheim installer](https://github.com/UB-Mannheim/tesseract/wiki) → add to PATH |
| 🍎 **macOS** | `brew install tesseract` |
| 🐧 **Linux** | `sudo apt install tesseract-ocr` |

### 2️⃣ Clone & Install

```bash
git clone https://github.com/your-username/AI-Mental-Health-Chatbot-OCR-Scanner.git
cd AI-Mental-Health-Chatbot-OCR-Scanner
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS / Linux
cd backend && pip install -r requirements.txt
```

### 3️⃣ Launch

```bash
python app.py
# → http://127.0.0.1:5000
```

---

## 🔌 API Endpoint Reference

<div align="center">
<a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=14&pause=1200&color=6C63FF&center=true&vCenter=true&width=600&lines=Base+URL+%3A+http%3A%2F%2Flocalhost%3A5000%2Fapi;All+responses+%3A+Content-Type%3A+application%2Fjson;CORS+enabled+%3A+all+origins" alt="API Base" /></a>
</div>

<br/>

---

### 💬 Emotion Analysis — NLP Operations

<table>
<tr>
<td width="100%">

| | |
|---|---|
| ![POST](https://img.shields.io/badge/POST-grey?style=flat-square&labelColor=555) &nbsp; ![/api/chat](https://img.shields.io/badge/%2Fapi%2Fchat-1db954?style=flat-square) | ![AUTH](https://img.shields.io/badge/AUTH-grey?style=flat-square&labelColor=555) &nbsp; ![NOT REQUIRED](https://img.shields.io/badge/NOT%20REQUIRED-2ecc71?style=flat-square) |

**Analyze free-text for emotional state using transformer-based NLP classification**

| Field | Value |
|:------|:------|
| **Method** | ![POST](https://img.shields.io/badge/POST-555?style=flat-square) |
| **URL** | `http://localhost:5000/api/chat` |
| **Content-Type** | `application/json` |
| **Returns** | Dominant emotion · confidence · risk level · AI advice |

```bash
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"I have been feeling really anxious and overwhelmed lately."}'
```

<details>
<summary>📤 Sample Response · <code>200 OK</code></summary>

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

</details>

**Response Schema**

| Field | Type | Description |
|:------|:----:|:------------|
| `dominant_emotion` | `string` | Highest-confidence predicted emotion label |
| `confidence` | `float` | Probability score 0–100 for dominant class |
| `risk_level` | `string` | `low` · `low-medium` · `medium` · `high` |
| `color` | `string` | UI color token mapped to emotion |
| `advice` | `string` | Personalised AI-generated mental health guidance |
| `all_emotions` | `array` | Full softmax probability distribution (sorted) |

> ![400](https://img.shields.io/badge/400-Bad_Request-e74c3c?style=flat-square) &nbsp; Missing or empty `message` field

</td>
</tr>
</table>

<br/>

---

### 📄 Medical Report Scanner — OCR Operations

<table>
<tr>
<td width="100%">

| | |
|---|---|
| ![POST](https://img.shields.io/badge/POST-grey?style=flat-square&labelColor=555) &nbsp; ![/api/ocr](https://img.shields.io/badge/%2Fapi%2Focr-8e44ad?style=flat-square) | ![AUTH](https://img.shields.io/badge/AUTH-grey?style=flat-square&labelColor=555) &nbsp; ![NOT REQUIRED](https://img.shields.io/badge/NOT%20REQUIRED-2ecc71?style=flat-square) |

**Upload a medical report image — extracts vitals, lab values, medications and diagnoses via computer vision OCR**

| Field | Value |
|:------|:------|
| **Method** | ![POST](https://img.shields.io/badge/POST-555?style=flat-square) |
| **URL** | `http://localhost:5000/api/ocr` |
| **Content-Type** | `multipart/form-data` |
| **Returns** | Structured patient data · vitals · labs · medications · diagnoses |

```bash
curl -X POST http://localhost:5000/api/ocr \
  -F "file=@/path/to/medical_report.png"
```

<details>
<summary>📤 Sample Response · <code>200 OK</code></summary>

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
    "raw_text":    "..."
  }
}
```

</details>

**Extraction Schema**

| Field | Type | Extraction Method |
|:------|:----:|:------------------|
| `patient_name` | `string \| null` | Heuristic label scan: `Patient:` / `Name:` |
| `date` | `string \| null` | Regex: `DD/MM/YYYY` · `MM-DD-YY` · `DD-MM-YYYY` |
| `vitals` | `object` | Regex: `BP` · `HR` · `Temp` · `SpO2` · `BMI` · `Weight` |
| `lab_values` | `object` | Regex: `HbA1c` · `Glucose` · `WBC` · `RBC` · `TSH` · `T3` · `T4` |
| `medications` | `array` | Lines containing dosage units: `mg` · `mcg` · `ml` |
| `diagnoses` | `array` | Lines matching: `diagnosis` · `impression` · `assessment` |

> ![400](https://img.shields.io/badge/400-No_File-e74c3c?style=flat-square) &nbsp; No file attached &nbsp;&nbsp; ![400](https://img.shields.io/badge/400-Empty_Filename-e74c3c?style=flat-square) &nbsp; File field present but empty

</td>
</tr>
</table>

<br/>

---

### 🔗 Combined Intelligence — Fusion Operations

<table>
<tr>
<td width="100%">

| | |
|---|---|
| ![POST](https://img.shields.io/badge/POST-grey?style=flat-square&labelColor=555) &nbsp; ![/api/analyze](https://img.shields.io/badge/%2Fapi%2Fanalyze-e67e22?style=flat-square) | ![AUTH](https://img.shields.io/badge/AUTH-grey?style=flat-square&labelColor=555) &nbsp; ![NOT REQUIRED](https://img.shields.io/badge/NOT%20REQUIRED-2ecc71?style=flat-square) |

**Full-stack intelligence — emotion NLP + OCR extraction + medical cross-reference correlation in one call**

| Field | Value |
|:------|:------|
| **Method** | ![POST](https://img.shields.io/badge/POST-555?style=flat-square) |
| **URL** | `http://localhost:5000/api/analyze` |
| **Content-Type** | `multipart/form-data` |
| **Returns** | Emotion analysis + OCR result + cross-reference matches |

```bash
curl -X POST http://localhost:5000/api/analyze \
  -F "message=I feel exhausted and completely hopeless" \
  -F "file=@/path/to/medical_report.png"
```

<details>
<summary>📤 Sample Response · <code>200 OK</code></summary>

```json
{
  "status": "success",
  "emotion_analysis": {
    "dominant_emotion": "sadness",
    "confidence": 84.2,
    "risk_level": "medium",
    "color": "blue",
    "advice": "Feelings of sadness are valid. Consider reaching out to a friend or therapist."
  },
  "ocr_result": {
    "diagnoses": ["Impression: Major Depressive Disorder"],
    "medications": ["Sertraline 50mg daily"]
  },
  "cross_reference": {
    "condition_matches": [
      {
        "condition": "depression",
        "matched_symptoms": ["hopelessness", "fatigue", "low energy"],
        "known_medications": ["Sertraline", "Fluoxetine", "Bupropion"],
        "recommendation": "Consult a psychiatrist for a full clinical evaluation."
      }
    ],
    "emotion_health_correlation": "⚠️ Your emotional state aligns with detected medical indicators. Professional consultation is strongly advised.",
    "total_matches": 1
  }
}
```

</details>

**Cross-Reference Logic**

| Trigger Condition | Output |
|:------------------|:-------|
| `emotion` = `sadness` or `fear` + depression/anxiety in report | ⚠️ Strong clinical correlation warning |
| `risk_level` = `high` | 🔴 Immediate professional referral message |
| Medical keyword matches found | 📋 Recommendations surfaced from DB |
| No matches + low risk | ✅ Continue monitoring your wellbeing |

> ![400](https://img.shields.io/badge/400-Bad_Request-e74c3c?style=flat-square) &nbsp; Neither `message` nor `file` provided

</td>
</tr>
</table>

<br/>

---

### ⚙️ System — Health & Monitoring

<table>
<tr>
<td width="100%">

| | |
|---|---|
| ![GET](https://img.shields.io/badge/GET-grey?style=flat-square&labelColor=555) &nbsp; ![/api/health](https://img.shields.io/badge/%2Fapi%2Fhealth-2980b9?style=flat-square) | ![AUTH](https://img.shields.io/badge/AUTH-grey?style=flat-square&labelColor=555) &nbsp; ![NOT REQUIRED](https://img.shields.io/badge/NOT%20REQUIRED-2ecc71?style=flat-square) |

**Service liveness probe — integrate with Docker HEALTHCHECK, Prometheus, or UptimeRobot for production monitoring**

| Field | Value |
|:------|:------|
| **Method** | ![GET](https://img.shields.io/badge/GET-2980b9?style=flat-square) |
| **URL** | `http://localhost:5000/api/health` |
| **Content-Type** | `application/json` |
| **Returns** | Service status confirmation |

```bash
curl -X GET http://localhost:5000/api/health
```

<details>
<summary>📤 Sample Response · <code>200 OK</code></summary>

```json
{
  "status": "ok",
  "service": "Mental Health AI API"
}
```

</details>

> 💡 Use this endpoint in **Docker** `HEALTHCHECK`, **GitHub Actions** smoke tests, or **UptimeRobot** ping monitors to verify API availability in CI/CD and production deployments.

</td>
</tr>
</table>

---

## 📦 Full Tech Stack

| Layer | Tool / Library | Version | Role |
|:------|:--------------|:-------:|:-----|
| 🧠 **Transformer Model** | `distilroberta-base` (HuggingFace) | — | Real-time emotion NLP inference |
| 🐍 **Web Framework** | `Flask` | 2.x | Lightweight production REST API |
| 🔗 **CORS Middleware** | `flask-cors` | latest | Cross-origin request handling |
| 🖼️ **OCR Engine** | `pytesseract` | latest | Computer vision text extraction |
| 🖼️ **Image Processing** | `Pillow` (PIL) | latest | Grayscale preprocessing for OCR accuracy |
| 📡 **ML Pipeline** | `transformers` (HuggingFace) | 4.x | NLP model loading + tokenisation |
| 🌐 **Frontend SPA** | Vanilla HTML/CSS/JS | — | Dark-mode single-page application |
| 🔒 **Code Quality** | `flake8` + `pre-commit` | — | PEP8 enforcement + secret scanning |

---

## 🪝 Pre-commit Hook Pipeline

```
🔍  detect private key ...................... ✅  Passed
🌿  don't commit to branch .................. ✅  Passed
🐍  flake8 .................................. ✅  Passed   ← E302 · E501 · E741 all resolved
📝  codespell ............................... ✅  Passed
🔐  mask secrets in staged files ............ ✅  Passed
⚙️   syntax and compile check ................ ✅  Passed
```

---

## ⚠️ Medical & Ethical Disclaimer

> [!CAUTION]
> This project is built for **educational, research, and portfolio demonstration purposes only**.
> It is **not a certified medical device** and must **not** be used as a substitute for professional psychological or clinical advice, diagnosis, or treatment.
> If you or someone you know is experiencing a mental health crisis, please contact a qualified healthcare professional or a crisis helpline **immediately**.

---

## 🤝 Contributing

```bash
git checkout -b feature/your-feature-name
git commit -m "feat: describe your change clearly"
git push origin feature/your-feature-name
# Open a Pull Request on GitHub ↗
```

- ✅ Follow PEP8 — `flake8` enforced via pre-commit
- ✅ Write descriptive commit messages (`feat:` · `fix:` · `docs:`)
- ✅ Add docstrings to all new functions
- ✅ Test all endpoints with `curl` or Postman before submitting PR

---

<div align="center">

**📄 Licensed under the MIT License**

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:ff4d8d,50:6c63ff,100:00e5c8&height=130&section=footer" width="100%"/>

</div>
