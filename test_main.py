from fastapi.testclient import TestClient
from main import app
import os
import train

if not os.path.exists("model.joblib"):
  train.train_model()

client = TestClient(app)


def test_health_check():
  response = client.get("/health")
  assert response.status_code == 200
  assert response.json() == {"status": "ok", "model_loaded": True}


def test_prediction_valid():
  payload = {"tenure": 12, "monthly_charges": 70.5, "total_charges": 846.0}
  response = client.post("/predict", json=payload)
  assert response.status_code == 200
  data = response.json()
  assert "churn_prediction" in data
  assert "churn_probability" in data
  assert data["churn_prediction"] in [0, 1]


def test_prediction_invalid_input():
  payload = {"tenure": -5, "monthly_charges": 70.5, "total_charges": 846.0}
  response = client.post("/predict", json=payload)
  assert response.status_code == 422