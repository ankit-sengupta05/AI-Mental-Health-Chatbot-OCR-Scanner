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
![NLP](https://img.shields.io/badge/NLP-DistilRoBERTa-orange?style=for-the-badge&logo=pytorch&logoColor=white)

<br/>

> **🧠 Emotion intelligence meets clinical data** — production-ready NLP sentiment analysis pipeline powered by `DistilRoBERTa` + structured medical report extraction via `Pytesseract OCR` + intelligent cross-referencing against a curated medical conditions database — all served through a blazing-fast **Flask REST API**.

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

> **Model:** `j-hartmann/emotion-english-distilroberta-base` · 124M parameters · fine-tuned across 6 diverse emotion datasets · state-of-the-art affective computing NLP

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
> The `UNEXPECTED` key warning for `roberta.embeddings.position_ids` during model load is **harmless** — it is a known cross-architecture artifact when loading RoBERTa checkpoints across task heads and can be safely ignored.

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

## 🚀 Quick Start — Local Development

### 1️⃣ Prerequisites

> ⚠️ **Tesseract OCR** must be installed on your system `PATH` before launching:

| Platform | Command |
|:--------:|:--------|
| 🪟 **Windows** | [UB-Mannheim installer](https://github.com/UB-Mannheim/tesseract/wiki) → add `tesseract.exe` to system PATH |
| 🍎 **macOS** | `brew install tesseract` |
| 🐧 **Linux / Ubuntu** | `sudo apt install tesseract-ocr` |

### 2️⃣ Clone & Install

```bash
git clone https://github.com/your-username/AI-Mental-Health-Chatbot-OCR-Scanner.git
cd AI-Mental-Health-Chatbot-OCR-Scanner

# Create virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS / Linux

# Install dependencies
cd backend && pip install -r requirements.txt
```

### 3️⃣ Launch Backend

```bash
python app.py
```

```
Loading weights: 100%|█████████████████████| 105/105
RobertaForSequenceClassification loaded ✅
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

> First run downloads DistilRoBERTa weights (~300 MB) automatically from HuggingFace Hub.

### 4️⃣ Open Frontend

```bash
python -m http.server 8080 --directory frontend
# → http://localhost:8080
```

---

## 🔌 API Reference

<div align="center">

**Base URL** &nbsp;`http://localhost:5000/api` &nbsp;·&nbsp; All responses · `Content-Type: application/json`

</div>

---

<!--────────────────────────── POST /api/chat ──────────────────────────-->

<table>
<tr>
<td>

<img src="https://img.shields.io/badge/POST-%2Fapi%2Fchat-1db954?style=for-the-badge&labelColor=0d1117&color=1db954" />
&nbsp;&nbsp;
<img src="https://img.shields.io/badge/NLP-Emotion_Analysis-00e5c8?style=flat-square" />
<img src="https://img.shields.io/badge/Model-DistilRoBERTa-6c63ff?style=flat-square" />
<img src="https://img.shields.io/badge/Output-7_Emotion_Classes-ff4d8d?style=flat-square" />

**Analyze free-text input for emotional state using transformer-based NLP sentiment classification**

**📥 Request**
```http
POST /api/chat
Content-Type: application/json
```
```json
{
  "message": "I've been feeling really anxious and overwhelmed lately."
}
```

**📤 Response · `200 OK`**
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

**📋 Response Schema**

| Field | Type | Description |
|:------|:----:|:------------|
| `dominant_emotion` | `string` | Highest-confidence predicted emotion label |
| `confidence` | `float` | Probability score 0–100 for dominant class |
| `risk_level` | `string` | `low` · `low-medium` · `medium` · `high` |
| `color` | `string` | UI color token mapped to emotion |
| `advice` | `string` | Personalised AI-generated mental health guidance |
| `all_emotions` | `array` | Full softmax probability distribution (sorted) |

**⚡ Error Responses**

- ![400](https://img.shields.io/badge/400-Bad_Request-e74c3c?style=flat-square) — Missing or empty `message` field

</td>
</tr>
</table>

---

<!--────────────────────────── POST /api/ocr ──────────────────────────-->

<table>
<tr>
<td>

<img src="https://img.shields.io/badge/POST-%2Fapi%2Focr-8e44ad?style=for-the-badge&labelColor=0d1117&color=8e44ad" />
&nbsp;&nbsp;
<img src="https://img.shields.io/badge/OCR-Pytesseract-4285F4?style=flat-square" />
<img src="https://img.shields.io/badge/Input-PNG_JPG_TIFF-FFD21E?style=flat-square" />
<img src="https://img.shields.io/badge/Parser-Regex_NLP-00e5c8?style=flat-square" />

**Upload a medical report image — extracts and structures vitals, lab values, medications, and diagnoses via computer vision OCR**

**📥 Request**
```http
POST /api/ocr
Content-Type: multipart/form-data
```
```
file:  <image/png | image/jpeg | image/tiff>
```

**📤 Response · `200 OK`**
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

**📋 Extraction Schema**

| Field | Type | Extraction Method |
|:------|:----:|:------------------|
| `patient_name` | `string \| null` | Heuristic label scan: `Patient:` / `Name:` |
| `date` | `string \| null` | Regex: `DD/MM/YYYY` · `MM-DD-YY` · `DD-MM-YYYY` |
| `vitals` | `object` | Regex: `BP` · `HR` · `Temp` · `SpO2` · `BMI` · `Weight` |
| `lab_values` | `object` | Regex: `HbA1c` · `Glucose` · `WBC` · `RBC` · `TSH` · `T3` · `T4` |
| `medications` | `array` | Lines containing dosage units: `mg` · `mcg` · `ml` |
| `diagnoses` | `array` | Lines matching: `diagnosis` · `impression` · `assessment` |

**⚡ Error Responses**

- ![400](https://img.shields.io/badge/400-No_File-e74c3c?style=flat-square) — No file attached to request
- ![400](https://img.shields.io/badge/400-Empty_Filename-e74c3c?style=flat-square) — File field present but filename empty

</td>
</tr>
</table>

---

<!--────────────────────────── POST /api/analyze ──────────────────────────-->

<table>
<tr>
<td>

<img src="https://img.shields.io/badge/POST-%2Fapi%2Fanalyze-e67e22?style=for-the-badge&labelColor=0d1117&color=e67e22" />
&nbsp;&nbsp;
<img src="https://img.shields.io/badge/Combined-NLP_%2B_OCR_%2B_CrossRef-ff4d8d?style=flat-square" />
<img src="https://img.shields.io/badge/Engine-Medical_AI_Fusion-6c63ff?style=flat-square" />

**Full-stack analysis — runs emotion NLP classification + OCR document extraction + medical cross-reference correlation in a single intelligent API call**

**📥 Request**
```http
POST /api/analyze
Content-Type: multipart/form-data
```
```
message:  "I feel exhausted and completely hopeless"   (optional)
file:     <medical report image>                       (optional)
```

**📤 Response · `200 OK`**
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

**🔗 Cross-Reference Logic**

| Condition | Trigger | Output |
|:----------|:--------|:-------|
| `emotion` in `[sadness, fear]` + medical match | Depression / anxiety in report | ⚠️ Strong clinical correlation warning |
| `risk_level == high` | Any emotion state | 🔴 Immediate professional referral |
| Medical matches found | No high-risk emotion | 📋 Recommendations surfaced |
| No matches | Neutral / low risk | ✅ Continue monitoring |

**⚡ Error Responses**

- ![400](https://img.shields.io/badge/400-Bad_Request-e74c3c?style=flat-square) — Neither `message` nor `file` provided

</td>
</tr>
</table>

---

<!--────────────────────────── GET /api/health ──────────────────────────-->

<table>
<tr>
<td>

<img src="https://img.shields.io/badge/GET-%2Fapi%2Fhealth-2980b9?style=for-the-badge&labelColor=0d1117&color=2980b9" />
&nbsp;&nbsp;
<img src="https://img.shields.io/badge/Liveness-Health_Check-00e5c8?style=flat-square" />
<img src="https://img.shields.io/badge/Uptime-Monitoring-brightgreen?style=flat-square" />

**Service liveness probe — use in CI/CD pipelines, Docker health checks, or uptime monitors to verify the Flask API is running and responsive**

**📥 Request**
```http
GET /api/health
```

**📤 Response · `200 OK`**
```json
{
  "status": "ok",
  "service": "Mental Health AI API"
}
```

> 💡 Integrate with tools like **UptimeRobot**, **Prometheus**, or **Docker HEALTHCHECK** to monitor API availability in production deployments.

</td>
</tr>
</table>

---

## 📦 Full Tech Stack

| Layer | Tool / Library | Version | Role in Pipeline |
|:------|:--------------|:-------:|:-----------------|
| 🧠 **Transformer Model** | `distilroberta-base` (HuggingFace Hub) | — | Real-time emotion inference |
| 🐍 **Web Framework** | `Flask` | 2.x | Lightweight REST API server |
| 🔗 **CORS Middleware** | `flask-cors` | latest | Cross-origin request handling |
| 🖼️ **OCR Engine** | `pytesseract` | latest | Computer vision text extraction |
| 🖼️ **Image Processing** | `Pillow` (PIL) | latest | Grayscale preprocessing for OCR accuracy |
| 📡 **ML Inference Pipeline** | `transformers` (HuggingFace) | 4.x | NLP model loading + tokenisation |
| 🌐 **Frontend SPA** | Vanilla HTML / CSS / JS | — | Dark-mode single-page application |
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

> Run `pre-commit install` after cloning to activate all hooks locally.

---

## ⚠️ Medical & Ethical Disclaimer

> [!CAUTION]
> This project is built for **educational, research, and portfolio demonstration purposes only**.
> It is **not a certified medical device** and must **not** be used as a substitute for professional psychological or clinical advice, diagnosis, or treatment.
> If you or someone you know is experiencing a mental health crisis, please contact a qualified healthcare professional or a crisis helpline **immediately**.

---

## 🤝 Contributing

```bash
# Fork → Branch → Commit → PR
git checkout -b feature/your-feature-name
git commit -m "feat: describe your change clearly"
git push origin feature/your-feature-name
# Open a Pull Request on GitHub ↗
```

- ✅ Follow PEP8 (flake8 will enforce it via pre-commit)
- ✅ Write descriptive commit messages
- ✅ Add docstrings to new functions
- ✅ Test endpoints with Postman or `curl` before submitting

---

<div align="center">

**📄 Licensed under the MIT License**

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:ff4d8d,50:6c63ff,100:00e5c8&height=130&section=footer" width="100%"/>

</div>
