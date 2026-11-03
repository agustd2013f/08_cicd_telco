from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
import joblib
import numpy as np
from pydantic import BaseModel, Field

app = FastAPI(
    title="Telco Churn Prediction API",
    version="1.0.0",
    description="API REST para la predicción de abandono de clientes",
)


class CustomerData(BaseModel):
  tenure: int = Field(..., ge=0, description="Meses de permanencia")
  monthly_charges: float = Field(
      ..., ge=0.0, description="Cargos mensuales en USD"
  )
  total_charges: float = Field(
      ..., ge=0.0, description="Cargos acumulados en USD"
  )


try:
  model = joblib.load("model.joblib")
except Exception:
  model = None


@app.get("/", response_class=HTMLResponse)
def read_root():
  return """
    <!DOCTYPE html>
    <html>
        <head><title>Telco Churn API</title></head>
        <body style="font-family: Arial, sans-serif; margin: 40px;">
            <h2>Predicción de Churn - Telco</h2>
            <p>Estado del servicio: <strong>Activo</strong></p>
            <p>Documentación interactiva disponible en <a href="/docs">/docs</a></p>
        </body>
    </html>
    """


@app.get("/health")
def health_check():
  if model is None:
    raise HTTPException(
        status_code=503, detail="Modelo no disponible o no cargado"
    )
  return {"status": "ok", "model_loaded": True}


@app.post("/predict")
def predict(data: CustomerData):
  if model is None:
    raise HTTPException(status_code=503, detail="Modelo no disponible")

  features = np.array(
      [[data.tenure, data.monthly_charges, data.total_charges]]
  )
  prediction = int(model.predict(features)[0])
  probability = float(model.predict_proba(features)[0][1])

  return {
      "churn_prediction": prediction,
      "churn_probability": round(probability, 4),
      "status": "Churn" if prediction == 1 else "No Churn",
  }