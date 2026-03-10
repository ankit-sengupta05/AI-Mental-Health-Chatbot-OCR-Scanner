from flask import Flask, request, jsonify
from flask_cors import CORS
from sentiment_model import analyze_sentiment
from ocr_pipeline import extract_text_from_image, parse_medical_report
from medical_crossref import crossreference_report

app = Flask(__name__)
CORS(app)


@app.route('/api/chat', methods=['POST'])
def chat():
    """Analyze chat message for emotional state."""
    data = request.get_json()
    message = data.get('message', '').strip()
    if not message:
        return jsonify({"error": "No message provided"}), 400

    emotion_result = analyze_sentiment(message)
    return jsonify({
        "status": "success",
        "emotion_analysis": emotion_result,
        "message": message
    })


@app.route('/api/ocr', methods=['POST'])
def ocr_scan():
    """Process uploaded medical report image."""
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "Empty filename"}), 400

    image_bytes = file.read()
    raw_text = extract_text_from_image(image_bytes)
    parsed = parse_medical_report(raw_text)

    return jsonify({
        "status": "success",
        "ocr_result": parsed
    })


@app.route('/api/analyze', methods=['POST'])
def full_analysis():
    """Combined: emotion from message + OCR from report + cross-reference."""
    message = request.form.get('message', '').strip()
    file = request.files.get('file')

    if not message and not file:
        return jsonify({"error": "Provide a message and/or file"}), 400

    result = {}

    # Emotion analysis
    if message:
        result["emotion_analysis"] = analyze_sentiment(message)

    # OCR analysis
    if file:
        image_bytes = file.read()
        raw_text = extract_text_from_image(image_bytes)
        result["ocr_result"] = parse_medical_report(raw_text)

    # Cross-reference if both present
    if message and file:
        result["cross_reference"] = crossreference_report(
            result["ocr_result"],
            result["emotion_analysis"]
        )

    return jsonify({"status": "success", **result})


@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({"status": "ok", "service": "Mental Health AI API"})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
