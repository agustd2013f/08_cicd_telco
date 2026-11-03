# Telco Churn Prediction API

Proyecto modular de MLOps con FastAPI, Docker y GitHub Actions.

## Instrucciones rápidas
1. Crear entorno virtual: `python -m venv venv`
2. Activar entorno: `.\venv\Scripts\Activate.ps1`
3. Instalar librerías: `pip install -r requirements.txt`
4. Entrenar modelo: `python train.py`
5. Probar API: `pytest -v`
6. Levantar servicio: `uvicorn main:app --reload`