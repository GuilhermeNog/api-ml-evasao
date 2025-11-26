"""
Schemas Pydantic para previsões.
"""
from typing import List
from pydantic import BaseModel, Field
from app.schemas.student_schema import StudentInput


class PredictionOutput(BaseModel):
    """
    Schema de saída para uma previsão individual.
    """

    prob_evasao: float = Field(
        ..., description="Probabilidade de evasão (0.0 a 1.0)", example=0.78
    )
    classe_prevista: int = Field(
        ..., description="Classe prevista (0 = permanece, 1 = evade)", example=1
    )
    threshold: float = Field(
        ..., description="Threshold usado para classificação", example=0.5
    )

    class Config:
        schema_extra = {
            "example": {
                "prob_evasao": 0.78,
                "classe_prevista": 1,
                "threshold": 0.5,
            }
        }


class BatchPredictionInput(BaseModel):
    """
    Schema de entrada para previsão em lote.
    """

    alunos: List[StudentInput] = Field(..., description="Lista de alunos para previsão")

    class Config:
        schema_extra = {
            "example": {
                "alunos": [
                    {
                        "idade": 19,
                        "sexo": "F",
                        "tipo_escola_medio": "publica",
                        "nota_enem": 650.5,
                        "renda_familiar": 2500.0,
                        "trabalha": 1,
                        "horas_trabalho_semana": 30,
                        "reprovacoes_1_sem": 2,
                        "bolsista": 0,
                        "distancia_campus_km": 12.3,
                    },
                    {
                        "idade": 22,
                        "sexo": "M",
                        "tipo_escola_medio": "privada",
                        "nota_enem": 720.0,
                        "renda_familiar": 5000.0,
                        "trabalha": 0,
                        "horas_trabalho_semana": 0,
                        "reprovacoes_1_sem": 0,
                        "bolsista": 1,
                        "distancia_campus_km": 5.0,
                    },
                ]
            }
        }


class BatchPredictionOutput(BaseModel):
    """
    Schema de saída para previsão em lote.
    """

    previsoes: List[PredictionOutput] = Field(..., description="Lista de previsões")

    class Config:
        schema_extra = {
            "example": {
                "previsoes": [
                    {"prob_evasao": 0.82, "classe_prevista": 1, "threshold": 0.5},
                    {"prob_evasao": 0.12, "classe_prevista": 0, "threshold": 0.5},
                ]
            }
        }
