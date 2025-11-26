"""
Controller de previsão - orquestra a lógica de negócio.
Recebe dados, chama o serviço de ML e aplica regras de negócio.
"""
from typing import List
from app.schemas.student_schema import StudentInput
from app.schemas.prediction_schema import (
    PredictionOutput,
    BatchPredictionInput,
)
from app.services import ml_service
from app.core.config import PREDICTION_THRESHOLD


def predict_single(student: StudentInput) -> PredictionOutput:
    """
    Faz previsão para um único aluno.
    
    Args:
        student: Dados do aluno (StudentInput schema)
    
    Returns:
        PredictionOutput com probabilidade, classe prevista e threshold
    """
    # Converte o StudentInput (Pydantic) para dicionário
    student_dict = student.dict()
    
    # Chama o serviço de ML para obter a probabilidade
    prob_evasao = ml_service.predict_proba_single(student_dict)
    
    # Aplica o threshold para determinar a classe
    classe_prevista = 1 if prob_evasao >= PREDICTION_THRESHOLD else 0
    
    # Retorna o resultado estruturado
    return PredictionOutput(
        prob_evasao=prob_evasao,
        classe_prevista=classe_prevista,
        threshold=PREDICTION_THRESHOLD,
    )


def predict_multiple(batch: BatchPredictionInput) -> List[PredictionOutput]:
    """
    Faz previsão para múltiplos alunos.
    
    Args:
        batch: BatchPredictionInput contendo lista de alunos
    
    Returns:
        Lista de PredictionOutput
    """
    # Extrai a lista de alunos
    students = batch.alunos
    
    # Converte cada aluno para dicionário
    students_dicts = [student.dict() for student in students]
    
    # Chama o serviço de ML para obter as probabilidades em lote
    probabilities = ml_service.predict_proba_batch(students_dicts)
    
    # Para cada probabilidade, cria um PredictionOutput
    predictions = []
    for prob_evasao in probabilities:
        classe_prevista = 1 if prob_evasao >= PREDICTION_THRESHOLD else 0
        
        predictions.append(
            PredictionOutput(
                prob_evasao=prob_evasao,
                classe_prevista=classe_prevista,
                threshold=PREDICTION_THRESHOLD,
            )
        )
    
    return predictions
