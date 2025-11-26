import joblib
from pathlib import Path
import sklearn
from sklearn.compose._column_transformer import _RemainderColsList

# Testa importar
MODEL_PATH = Path("model/logistic_model.pkl")

print(f"_RemainderColsList: {_RemainderColsList}")
print(f"Tentando carregar modelo de: {MODEL_PATH}")

try:
    model = joblib.load(MODEL_PATH)
    print(f"✅ Sucesso! Tipo: {type(model)}")
except Exception as e:
    print(f"❌ Erro: {e}")
    import traceback
    traceback.print_exc()
