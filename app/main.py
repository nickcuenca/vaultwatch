from fastapi import FastAPI
from app import database, auth, anomaly

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "VaultWatch running"}