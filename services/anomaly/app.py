from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Univote Anomaly Service")


class Event(BaseModel):
    features: List[float]


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/score")
def score(event: Event):
    # Placeholder: return simple anomaly score (e.g., z-score proxy)
    s = sum(abs(x) for x in event.features) / (len(event.features) or 1)
    return {"score": float(s)}

