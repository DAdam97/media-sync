import pytest
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_health():
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_protected_endpoint_without_key():
    response = client.get("/api/downloads")
    assert response.status_code == 403


def test_protected_endpoint_wrong_key(monkeypatch):
    import config
    monkeypatch.setattr(config.settings, "api_key", "correct-key")
    response = client.get("/api/downloads", headers={"Authorization": "Bearer wrong-key"})
    assert response.status_code == 401
