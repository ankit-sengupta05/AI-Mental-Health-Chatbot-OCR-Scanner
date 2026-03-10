import pytesseract
from PIL import Image
import re
import io


def extract_text_from_image(image_bytes: bytes) -> str:
    """Extract raw text from uploaded medical report image."""
    image = Image.open(io.BytesIO(image_bytes))
    # Enhance for better OCR
    image = image.convert('L')  # Grayscale
    raw_text = pytesseract.image_to_string(image, config='--psm 6')
    return raw_text.strip()


def parse_medical_report(raw_text: str) -> dict:
    """Structure extracted medical text into meaningful fields."""
    lines = [line.strip() for line in raw_text.split('\n') if line.strip()]

    parsed = {
        "raw_text": raw_text,
        "patient_name": None,
        "date": None,
        "diagnoses": [],
        "medications": [],
        "vitals": {},
        "lab_values": {},
        "notes": []
    }

    # Regex patterns
    date_pattern = re.compile(r'\b(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})\b')
    vitals_pattern = re.compile(
        r'(BP|Blood Pressure|Heart Rate|HR|Temp|Temperature|O2|SpO2|Weight|BMI)'
        r'[:\s]+([0-9./]+\s*\w*)',
        re.IGNORECASE
    )
    lab_pattern = re.compile(
        r'(HbA1c|Glucose|Cholesterol|Hemoglobin|WBC|RBC|Platelets|TSH|T3|T4)'
        r'[:\s]+([0-9.]+\s*\w*/?[\w]*)',
        re.IGNORECASE
    )
    med_pattern = re.compile(r'\b(mg|mcg|ml)\b', re.IGNORECASE)
    diagnosis_pattern = re.compile(
        r'\b(diagnosis|diagnoses|impression|assessment|condition)\b',
        re.IGNORECASE
    )

    for line in lines:
        # Date
        date_match = date_pattern.search(line)
        if date_match and not parsed["date"]:
            parsed["date"] = date_match.group(1)

        # Patient name (heuristic: "Patient:" or "Name:")
        if re.search(r'\b(patient|name)\b', line, re.IGNORECASE) and ':' in line:
            value = line.split(':', 1)[-1].strip()
            if value and len(value) < 60:
                parsed["patient_name"] = value

        # Vitals
        vitals_matches = vitals_pattern.findall(line)
        for k, v in vitals_matches:
            parsed["vitals"][k.strip()] = v.strip()

        # Lab values
        lab_matches = lab_pattern.findall(line)
        for k, v in lab_matches:
            parsed["lab_values"][k.strip()] = v.strip()

        # Medications (lines with dosage)
        if med_pattern.search(line) and len(line) < 100:
            parsed["medications"].append(line)

        # Diagnoses (lines with "diagnosis", "impression", "assessment")
        if diagnosis_pattern.search(line):
            parsed["diagnoses"].append(line)

    # Fallback: if no diagnoses found, flag notable lines
    if not parsed["diagnoses"]:
        parsed["notes"] = lines[:5]  # First 5 lines as notes

    return parsed
