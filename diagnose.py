import joblib
from pathlib import Path
import sys

MODEL_PATH = Path("model/logistic_model.pkl")

print(f"Python: {sys.version}")
print(f"Joblib version: {joblib.__version__}")

# Tenta carregar com mais detalhes
print(f"\nCarregando de: {MODEL_PATH.absolute()}")

try:
    import sklearn
    print(f"sklearn version: {sklearn.__version__}")
    
    # Importa TUDO possível
    from sklearn import *
    import sklearn.compose
    from sklearn.compose import ColumnTransformer
    
    # Agora tenta carregar
    model = joblib.load(MODEL_PATH)
    print(f"\n✅ SUCESSO!")
    print(f"Tipo: {type(model)}")
    
except Exception as e:
    print(f"\n❌ ERRO: {e}")
    import traceback
    traceback.print_exc()
