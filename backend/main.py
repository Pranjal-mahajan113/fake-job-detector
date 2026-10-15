
from fastapi import FastAPI

from routes.prediction import router as prediction_router

app = FastAPI(
    title="Fake Job Detector API",
    description="API for detecting potentially fake job postings using machine learning.",
    version="1.0.0",
)

# Register prediction routes
app.include_router(prediction_router)


@app.get("/")
def home():
    return {
        "message": "Fake Job Detector API is running!"
    }
