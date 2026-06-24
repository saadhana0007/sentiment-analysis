# Sentiment Analysis API

Analyze any text and get back a sentiment label (`POSITIVE` / `NEGATIVE` / `NEUTRAL`) with a confidence score, in real time, using a pre-trained HuggingFace NLP model.

## Tech Stack
- Python
- FastAPI
- HuggingFace Transformers (`distilbert-base-uncased-finetuned-sst-2-english`)
- Uvicorn

## Features
- `POST /analyze` — analyze a single piece of text
- `POST /analyze/batch` — analyze a list of texts in one request
- `GET /health` — health check endpoint
- Input validation — empty strings are rejected
- Low-confidence predictions are labeled `NEUTRAL` instead of forcing a binary call

## Getting Started

### Prerequisites
- Python 3.9+

### Installation
```bash
git clone https://github.com/saadhana0007/sentiment-analysis
cd sentiment-analysis
pip install -r requirements.txt
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`. Interactive docs at `http://127.0.0.1:8000/docs`.

### Example

```bash
curl -X POST http://127.0.0.1:8000/analyze \
  -H "Content-Type: application/json" \
  -d '{"text": "I absolutely loved this!"}'
```

```json
{
  "text": "I absolutely loved this!",
  "label": "POSITIVE",
  "score": 0.9998
}
```

Batch request:

```bash
curl -X POST http://127.0.0.1:8000/analyze/batch \
  -H "Content-Type: application/json" \
  -d '{"texts": ["I loved it!", "This was terrible."]}'
```

## Project Structure
```
sentiment-analysis/
├── main.py              # FastAPI app and routes
├── model.py             # Loads and runs the HuggingFace sentiment model
├── schemas.py           # Request/response models
├── test_main.py         # API tests
├── requirements.txt
└── README.md
```

## Tests
```bash
pip install pytest httpx
pytest
```
