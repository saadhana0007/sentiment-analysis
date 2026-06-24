from fastapi import FastAPI

from model import analyze, analyze_batch
from schemas import (
    AnalyzeRequest,
    AnalyzeResponse,
    BatchAnalyzeRequest,
    BatchAnalyzeResponse,
)

app = FastAPI(
    title="Sentiment Analysis API",
    description="Analyze text and return a sentiment label (POSITIVE/NEGATIVE/NEUTRAL) with a confidence score.",
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/analyze", response_model=AnalyzeResponse)
def analyze_text(request: AnalyzeRequest):
    return analyze(request.text)


@app.post("/analyze/batch", response_model=BatchAnalyzeResponse)
def analyze_texts(request: BatchAnalyzeRequest):
    return {"results": analyze_batch(request.texts)}
