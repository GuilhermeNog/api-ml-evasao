"""
Configurações centrais da aplicação.
"""
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
API_VERSION = "1.0.0"
MODEL_PATH = BASE_DIR / "model" / "logistic_model.pkl"
PREDICTION_THRESHOLD = 0.5
