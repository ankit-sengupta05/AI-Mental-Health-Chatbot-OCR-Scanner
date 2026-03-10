from transformers import pipeline

# Load pre-trained sentiment/emotion model (no training needed)
emotion_classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    return_all_scores=True
)

EMOTION_MENTAL_MAP = {
    "joy": {
        "risk": "low",
        "color": "green",
        "advice": "You seem to be in a positive emotional state. Keep maintaining healthy routines."
    },
    "sadness": {
        "risk": "medium",
        "color": "blue",
        "advice": "Feelings of sadness are valid. Consider reaching out to a friend or therapist."
    },
    "anger": {
        "risk": "medium",
        "color": "orange",
        "advice": "Anger can signal unmet needs. Deep breathing and journaling may help."
    },
    "fear": {
        "risk": "high",
        "color": "red",
        "advice": (
            "Fear and anxiety are linked. "
            "Grounding techniques and professional support are recommended."
        )
    },
    "disgust": {
        "risk": "low-medium",
        "color": "yellow",
        "advice": (
            "These feelings may indicate boundary violations. "
            "Reflect and consider counseling."
        )
    },
    "surprise": {
        "risk": "low",
        "color": "teal",
        "advice": "Emotional surprise is normal. Take time to process any unexpected events."
    },
    "neutral": {
        "risk": "low",
        "color": "gray",
        "advice": "You appear emotionally balanced. Stay consistent with self-care practices."
    }
}


def analyze_sentiment(text: str) -> dict:
    results = emotion_classifier(text)[0]
    # Sort by score, get dominant emotion
    sorted_emotions = sorted(results, key=lambda x: x['score'], reverse=True)
    dominant = sorted_emotions[0]
    emotion_label = dominant['label'].lower()
    confidence = round(dominant['score'] * 100, 1)

    mental_info = EMOTION_MENTAL_MAP.get(emotion_label, EMOTION_MENTAL_MAP["neutral"])

    return {
        "dominant_emotion": emotion_label,
        "confidence": confidence,
        "risk_level": mental_info["risk"],
        "color": mental_info["color"],
        "advice": mental_info["advice"],
        "all_emotions": [
            {"label": e['label'].lower(), "score": round(e['score'] * 100, 1)}
            for e in sorted_emotions
        ]
    }
