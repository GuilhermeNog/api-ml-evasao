"""
Schema Pydantic para entrada de dados do estudante.
"""
from pydantic import BaseModel, Field


class StudentInput(BaseModel):
    """
    Schema de entrada para dados de um estudante.
    Usado para receber dados via API.
    """

    idade: int = Field(..., description="Idade do aluno em anos", example=19)
    sexo: str = Field(..., description="Sexo do aluno (M ou F)", example="F")
    tipo_escola_medio: str = Field(
        ..., description="Tipo de escola do ensino médio (publica ou privada)", example="publica"
    )
    nota_enem: float = Field(..., description="Nota do ENEM", example=650.5)
    renda_familiar: float = Field(..., description="Renda familiar em reais", example=2500.0)
    trabalha: int = Field(..., description="Se o aluno trabalha (0 = não, 1 = sim)", example=1)
    horas_trabalho_semana: int = Field(
        ..., description="Horas de trabalho por semana", example=30
    )
    reprovacoes_1_sem: int = Field(
        ..., description="Número de reprovações no primeiro semestre", example=2
    )
    bolsista: int = Field(..., description="Se o aluno é bolsista (0 = não, 1 = sim)", example=0)
    distancia_campus_km: float = Field(
        ..., description="Distância do campus em km", example=12.3
    )

    class Config:
        schema_extra = {
            "example": {
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
            }
        }
