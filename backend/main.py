
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.prediction import router as prediction_router

app = FastAPI(
    title="Fake Job Detector API",
    description="API for detecting potentially fake job postings using machine learning.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)

# Register prediction routes
app.include_router(prediction_router)


@app.get("/")
def home():
    return {
        "message": "Fake Job Detector API is running!"
    }
