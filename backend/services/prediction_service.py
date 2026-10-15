
import sys
from pathlib import Path

# Project root ko Python import path mein add karo
PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from ml.src.predictor import predict_job


def get_job_prediction(job_text: str) -> dict:
    """Call the ML predictor and return its result."""
    return predict_job(job_text)
