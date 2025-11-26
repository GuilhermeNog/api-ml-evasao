import joblib
from pathlib import Path
# Import ALL sklearn modules that might be needed
import sklearn
import sklearn.pipeline
import sklearn.preprocessing  
import sklearn.compose
import sklearn.linear_model

# Tenta carregar o modelo
MODEL_PATH = Path("model/logistic_model.pkl")

print(f"Caminho do modelo: {MODEL_PATH}")
print(f"Arquivo existe: {MODEL_PATH.exists()}")
print(f"Caminho absoluto: {MODEL_PATH.absolute()}")

if MODEL_PATH.exists():
    try:
        model = joblib.load(MODEL_PATH)
        print(f"\n✅ Modelo carregado com sucesso!")
        print(f"Tipo do modelo: {type(model)}")
        print(f"Modelo: {model}")
    except Exception as e:
        print(f"\n❌ Erro ao carregar modelo: {e}")
        import traceback
        traceback.print_exc()
else:
    print("\n❌ Arquivo do modelo não encontrado!")
