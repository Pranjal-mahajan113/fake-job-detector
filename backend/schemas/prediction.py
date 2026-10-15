
from pydantic import BaseModel, Field


class PredictionRequest(BaseModel):
    job_text: str = Field(
        ...,
        min_length=1,
        description="The job description to analyze",
    )


class PredictionResponse(BaseModel):
    prediction: str
    fake_score: float
    threshold: float
    label: int
