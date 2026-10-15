
from fastapi import APIRouter, HTTPException

from schemas.prediction import PredictionRequest, PredictionResponse
from services.prediction_service import get_job_prediction

router = APIRouter(
    prefix="/api",
    tags=["Prediction"],
)


@router.post("/predict", response_model=PredictionResponse)
def predict_job_route(request: PredictionRequest):
    try:
        return get_job_prediction(request.job_text)
    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        ) from exc
