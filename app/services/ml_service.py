"""
Serviço de Machine Learning para carregar e usar o modelo.
"""
import joblib
import pandas as pd
from typing import List, Dict
import sys

# Import ALL sklearn modules that the model might need
import sklearn
import sklearn.pipeline
import sklearn.preprocessing
import sklearn.compose
import sklearn.linear_model
# Explicit imports for joblib deserialization
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

# WORKAROUND: Adiciona _RemainderColsList ao módulo se não existir
# Isso resolve problemas de compatibilidade entre versões do sklearn
import sklearn.compose._column_transformer as ct_module
if not hasattr(ct_module, '_RemainderColsList'):
    # Cria a classe _RemainderColsList como um alias para list
    ct_module._RemainderColsList = type('_RemainderColsList', (list,), {})
    sys.modules['sklearn.compose._column_transformer']._RemainderColsList = ct_module._RemainderColsList

from app.core.config import MODEL_PATH

# Cache global para o modelo (evita carregar múltiplas vezes)
_model = None


def load_model():
    """
    Carrega o modelo do disco se ainda não estiver carregado.
    Usa cache global para evitar múltiplos carregamentos.
    
    Returns:
        O modelo carregado (Pipeline do scikit-learn)
    
    Raises:
        Exception: Se houver erro ao carregar o modelo
    """
    global _model
    
    if _model is None:
        try:
            _model = joblib.load(MODEL_PATH)
            print(f"✅ Modelo carregado com sucesso de: {MODEL_PATH}")
        except Exception as e:
            print(f"❌ Erro ao carregar modelo: {e}")
            raise e
    
    return _model


def predict_proba_single(features: Dict) -> float:
    """
    Faz previsão de probabilidade para um único aluno.
    
    Args:
        features: Dicionário com as features do aluno
    
    Returns:
        Probabilidade de evasão (classe 1)
    
    Raises:
        Exception: Se houver erro na previsão
    """
    try:
        # Carrega o modelo (usa cache se já carregado)
        model = load_model()
        
        # Converte o dicionário para DataFrame (necessário para o pipeline)
        df = pd.DataFrame([features])
        
        # Faz a previsão de probabilidade
        # predict_proba retorna array [[prob_classe_0, prob_classe_1]]
        # Queremos a probabilidade da classe 1 (evasão)
        prob_evasao = model.predict_proba(df)[0, 1]
        
        return float(prob_evasao)
    
    except Exception as e:
        print(f"❌ Erro na previsão: {e}")
        raise e


def predict_proba_batch(features_list: List[Dict]) -> List[float]:
    """
    Faz previsão de probabilidade para múltiplos alunos.
    
    Args:
        features_list: Lista de dicionários com features dos alunos
    
    Returns:
        Lista de probabilidades de evasão
    
    Raises:
        Exception: Se houver erro na previsão
    """
    try:
        # Carrega o modelo (usa cache se já carregado)
        model = load_model()
        
        # Converte a lista de dicionários para DataFrame
        df = pd.DataFrame(features_list)
        
        # Faz a previsão de probabilidade
        # predict_proba retorna array Nx2, queremos a coluna 1 (probabilidade de evasão)
        probabilities = model.predict_proba(df)[:, 1]
        
        # Converte numpy array para lista de floats
        return [float(prob) for prob in probabilities]
    
    except Exception as e:
        print(f"❌ Erro na previsão em lote: {e}")
        raise e
