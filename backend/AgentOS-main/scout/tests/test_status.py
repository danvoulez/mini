
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_status():
    response = client.get("/status")
    assert response.status_code == 200
    assert "status" in response.json()
