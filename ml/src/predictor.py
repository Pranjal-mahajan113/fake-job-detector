import joblib
from pathlib import Path

# Project paths
ML_DIR = Path(__file__).resolve().parents[1]
MODELS_DIR = ML_DIR / "models"

# Load the final model artifact
MODEL_PATH = MODELS_DIR / "final_fake_job_detector.joblib"
artifact = joblib.load(MODEL_PATH)

# Load model and threshold from the same artifact
model = artifact["model"]
THRESHOLD = artifact["threshold"]


def predict_job(job_text: str) -> dict:
    """Predict whether a job posting is fake or real."""

    if not isinstance(job_text, str) or not job_text.strip():
        raise ValueError("Job description cannot be empty.")

    fake_score = float(model.predict_proba([job_text])[0][1])

    prediction = int(fake_score >= THRESHOLD)

    return {
        "fake_score": round(fake_score, 4),
        "threshold": THRESHOLD,
        "prediction": "Fake Job" if prediction == 1 else "Real Job",
        "label": prediction,
    }
