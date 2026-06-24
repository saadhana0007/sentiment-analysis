from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_analyze_positive():
    response = client.post("/analyze", json={"text": "I love this product, it's amazing!"})
    assert response.status_code == 200
    body = response.json()
    assert body["label"] == "POSITIVE"
    assert 0 <= body["score"] <= 1


def test_analyze_rejects_empty_text():
    response = client.post("/analyze", json={"text": ""})
    assert response.status_code == 422


def test_analyze_batch():
    response = client.post(
        "/analyze/batch",
        json={"texts": ["I love this!", "I hate this."]},
    )
    assert response.status_code == 200
    body = response.json()
    assert len(body["results"]) == 2
