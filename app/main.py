"""
Aplicação principal FastAPI.
"""
from fastapi import FastAPI
from app.core.config import API_VERSION
from app.views.prediction_view import router as prediction_router

# Cria a aplicação FastAPI
app = FastAPI(
    title="API de Previsão de Evasão",
    version=API_VERSION,
    description="""
    API para previsão de evasão de alunos usando Machine Learning.
    
    Utiliza um modelo de Regressão Logística treinado em dataset de alunos
    para prever a probabilidade de evasão até o primeiro ano.
    
    ## Features
    - Previsão individual de evasão
    - Previsão em lote (múltiplos alunos)
    - Health check do modelo
    
    ## Modelo
    - Algoritmo: Regressão Logística com Pipeline scikit-learn
    - Features: idade, sexo, tipo_escola_medio, nota_enem, renda_familiar, 
      trabalha, horas_trabalho_semana, reprovacoes_1_sem, bolsista, distancia_campus_km
    - Target: evasao_ate_1ano (0 = permaneceu, 1 = evadiu)
    """,
)

# Inclui as rotas de previsão
app.include_router(prediction_router, prefix="")


@app.get("/", tags=["Root"])
def root():
    """
    Endpoint raiz da API.
    
    Returns:
        Mensagem de boas-vindas
    """
    return {
        "message": "API de Previsão de Evasão - OK",
        "version": API_VERSION,
        "docs": "/docs",
    }
