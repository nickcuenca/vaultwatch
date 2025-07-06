from fastapi import FastAPI
from app import database
from app.auth import router as auth_router
from app.anomaly import check_anomalies  # optional, for testing
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root route
@app.get("/")
def read_root():
    return {"status": "VaultWatch running"}

# Auth routes
app.include_router(auth_router)
