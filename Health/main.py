from fastapi import FastAPI
from app.models.health_model import HealthResponse

app = FastAPI()


@app.get("/health", response_model=HealthResponse)
def health():
    return {
        "status": "healthy"
    }