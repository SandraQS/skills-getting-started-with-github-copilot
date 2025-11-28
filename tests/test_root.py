import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_root_redirect():
    response = client.get("/")
    # Debe redirigir a /static/index.html
    assert response.status_code in (200, 307, 302)
    # Si es redirección, location debe ser /static/index.html
    if response.status_code in (307, 302):
        assert response.headers["location"].endswith("/static/index.html")
