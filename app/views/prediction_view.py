"""
Views (rotas) para previsão de evasão.
Define os endpoints da API.
"""
from fastapi import APIRouter, HTTPException
from app.schemas.student_schema import StudentInput
from app.schemas.prediction_schema import (
    PredictionOutput,
    BatchPredictionInput,
    BatchPredictionOutput,
)
from app.controllers import prediction_controller
from app.services import ml_service

# Cria o router
router = APIRouter()


@router.get("/health", tags=["Health"])
def health_check():
    """
    Endpoint de health check.
    Verifica se a API está rodando e se o modelo carrega corretamente.
    
    Returns:
        Dict com status e se o modelo está carregado
    """
    try:
        # Tenta carregar o modelo
        ml_service.load_model()
        model_loaded = True
    except Exception as e:
        print(f"⚠️ Modelo não carregou: {e}")
        model_loaded = False
    
    return {
        "status": "ok",
        "model_loaded": model_loaded,
    }


@router.post("/predict", response_model=PredictionOutput, tags=["Prediction"])
def predict(student: StudentInput):
    """
    Faz previsão de evasão para um único aluno.
    
    Args:
        student: Dados do aluno (StudentInput)
    
    Returns:
        PredictionOutput com probabilidade e classe prevista
    
    Raises:
        HTTPException: Se houver erro na previsão
    """
    try:
        # Chama o controller para fazer a previsão
        result = prediction_controller.predict_single(student)
        return result
    
    except Exception as e:
        # Em caso de erro, retorna HTTP 500
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/predict_batch", response_model=BatchPredictionOutput, tags=["Prediction"])
def predict_batch(batch: BatchPredictionInput):
    """
    Faz previsão de evasão para múltiplos alunos.
    
    Args:
        batch: BatchPredictionInput com lista de alunos
    
    Returns:
        BatchPredictionOutput com lista de previsões
    
    Raises:
        HTTPException: Se houver erro na previsão
    """
    try:
        # Chama o controller para fazer as previsões em lote
        predictions = prediction_controller.predict_multiple(batch)
        
        # Retorna no formato esperado
        return BatchPredictionOutput(previsoes=predictions)
    
    except Exception as e:
        # Em caso de erro, retorna HTTP 500
        raise HTTPException(status_code=500, detail=str(e))
