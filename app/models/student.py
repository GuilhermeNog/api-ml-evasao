"""
Entidade de domínio Student.
"""


class Student:

    def __init__(
        self,
        idade: int,
        sexo: str,
        tipo_escola_medio: str,
        nota_enem: float,
        renda_familiar: float,
        trabalha: int,
        horas_trabalho_semana: int,
        reprovacoes_1_sem: int,
        bolsista: int,
        distancia_campus_km: float,
    ):
        self.idade = idade
        self.sexo = sexo
        self.tipo_escola_medio = tipo_escola_medio
        self.nota_enem = nota_enem
        self.renda_familiar = renda_familiar
        self.trabalha = trabalha
        self.horas_trabalho_semana = horas_trabalho_semana
        self.reprovacoes_1_sem = reprovacoes_1_sem
        self.bolsista = bolsista
        self.distancia_campus_km = distancia_campus_km

    def __repr__(self):
        return f"Student(idade={self.idade}, sexo={self.sexo})"
