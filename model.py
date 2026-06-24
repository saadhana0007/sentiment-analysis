from functools import lru_cache

from transformers import pipeline

NEUTRAL_CONFIDENCE_THRESHOLD = 0.6


@lru_cache(maxsize=1)
def get_pipeline():
    return pipeline(
        "sentiment-analysis",
        model="distilbert-base-uncased-finetuned-sst-2-english",
    )


def analyze(text: str) -> dict:
    result = get_pipeline()(text)[0]
    label = result["label"]
    score = result["score"]

    if score < NEUTRAL_CONFIDENCE_THRESHOLD:
        label = "NEUTRAL"

    return {"text": text, "label": label, "score": round(score, 4)}


def analyze_batch(texts: list[str]) -> list[dict]:
    return [analyze(text) for text in texts]
