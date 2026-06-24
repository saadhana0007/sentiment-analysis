from pydantic import BaseModel, Field


class AnalyzeRequest(BaseModel):
    text: str = Field(..., min_length=1, description="Text to analyze")


class BatchAnalyzeRequest(BaseModel):
    texts: list[str] = Field(..., min_length=1, description="List of texts to analyze")


class AnalyzeResponse(BaseModel):
    text: str
    label: str
    score: float


class BatchAnalyzeResponse(BaseModel):
    results: list[AnalyzeResponse]
