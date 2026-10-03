from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.readings import router as readings_router


app = FastAPI(
    title="Water Quality Monitoring API",
    description="Real-time water quality monitoring backend",
    version="1.0.0"
)


# Allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Register water readings API
app.include_router(readings_router)


@app.get("/")
def root():
    return {
        "message": "Water Quality Monitoring API is running",
        "status": "success"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }