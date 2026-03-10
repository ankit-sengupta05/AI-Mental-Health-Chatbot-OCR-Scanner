import json
import os

# Load medical keywords dataset
DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'medical_keywords.json')

with open(DATA_PATH, 'r') as f:
    MEDICAL_DB = json.load(f)


def crossreference_report(parsed_report: dict, emotion_data: dict) -> dict:
    """Cross-reference OCR report data with medical DB and emotion state."""
    matches = []
    all_text = (
        ' '.join(parsed_report.get("diagnoses", [])) + ' ' +
        ' '.join(parsed_report.get("medications", [])) + ' ' +
        parsed_report.get("raw_text", "")
    ).lower()

    for condition, info in MEDICAL_DB.items():
        # Check symptoms in text
        matched_symptoms = [s for s in info["symptoms"] if s.lower() in all_text]
        if matched_symptoms or condition in all_text:
            matches.append({
                "condition": condition,
                "matched_symptoms": matched_symptoms,
                "known_medications": info["medications"],
                "recommendation": info["recommendations"]
            })

    # Emotion-health correlation
    emotion = emotion_data.get("dominant_emotion", "neutral")
    risk = emotion_data.get("risk_level", "low")

    depression_anxiety_match = any(
        m["condition"] in ["depression", "anxiety"] for m in matches
    )

    if emotion in ["sadness", "fear"] and depression_anxiety_match:
        correlation_note = (
            "⚠️ Your current emotional state aligns with detected medical indicators. "
            "Professional consultation is strongly advised."
        )
    elif risk == "high":
        correlation_note = (
            "🔴 High emotional distress detected. "
            "Please consider speaking with a mental health professional immediately."
        )
    elif matches:
        correlation_note = (
            "📋 Medical report indicators cross-referenced with emotional state. "
            "See recommendations below."
        )
    else:
        correlation_note = (
            "✅ No critical cross-references found. Continue monitoring your wellbeing."
        )

    return {
        "condition_matches": matches,
        "emotion_health_correlation": correlation_note,
        "total_matches": len(matches)
    }
