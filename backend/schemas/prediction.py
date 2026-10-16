
from pydantic import BaseModel, Field
from typing import Literal


class PredictionRequest(BaseModel):
    job_text: str = Field(
        ...,
        min_length=1,
        description="The job description to analyze",
    )


class PredictionResponse(BaseModel):
    prediction: Literal["Real Job", "Fake Job"]
    fake_score: float = Field(ge=0, le=1)
    threshold: float = Field(ge=0, le=1)
    label: Literal[0, 1]
