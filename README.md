# 🎓 API de Previsão de Evasão de Alunos

API REST desenvolvida com **FastAPI** seguindo o padrão **MVC** para servir um modelo de Machine Learning de previsão de evasão de alunos.

## 📋 Descrição

Esta API utiliza um modelo de **Regressão Logística** (scikit-learn) previamente treinado para prever a probabilidade de um aluno evadir até o primeiro ano do curso, com base em características socioeconômicas e acadêmicas.

### Features Utilizadas

- `idade`: Idade do aluno em anos
- `sexo`: Sexo do aluno ("M" ou "F")
- `tipo_escola_medio`: Tipo de escola do ensino médio ("publica" ou "privada")
- `nota_enem`: Nota do ENEM
- `renda_familiar`: Renda familiar em reais
- `trabalha`: Se o aluno trabalha (0 = não, 1 = sim)
- `horas_trabalho_semana`: Horas de trabalho por semana
- `reprovacoes_1_sem`: Número de reprovações no primeiro semestre
- `bolsista`: Se o aluno é bolsista (0 = não, 1 = sim)
- `distancia_campus_km`: Distância do campus em km

## 🏗️ Arquitetura

O projeto segue o padrão **MVC (Model-View-Controller)**:

```
app/
├── core/              # Configurações centrais
├── models/            # Entidades de domínio
├── schemas/           # Schemas Pydantic (validação)
├── services/          # Serviços (lógica de ML)
├── controllers/       # Controllers (orquestração)
└── views/             # Views (rotas FastAPI)
```

### Camadas

- **Model (M)**: Schemas Pydantic, entidades de domínio, serviço de ML
- **View (V)**: Rotas FastAPI (endpoints)
- **Controller (C)**: Lógica de orquestração e regras de negócio

## 🚀 Instalação

### Pré-requisitos

- Python 3.8+
- pip

### Passos

1. **Clone o repositório** (ou navegue até a pasta do projeto)

2. **Crie um ambiente virtual** (recomendado):

```bash
python -m venv venv
```

3. **Ative o ambiente virtual**:

Windows:
```bash
venv\Scripts\activate
```

Linux/Mac:
```bash
source venv/bin/activate
```

4. **Instale as dependências**:

```bash
pip install -r requirements.txt
```

## ▶️ Como Executar

Execute o servidor de desenvolvimento:

```bash
uvicorn app.main:app --reload
```

A API estará disponível em: **http://127.0.0.1:8000**

## 📚 Documentação Interativa

Após iniciar o servidor, acesse a documentação automática:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## 🔌 Endpoints

### GET `/` 
Endpoint raiz - retorna informações básicas da API

### GET `/health`
Health check - verifica se a API está rodando e se o modelo está carregado

**Resposta:**
```json
{
  "status": "ok",
  "model_loaded": true
}
```

### POST `/predict`
Previsão individual de evasão

**Request Body:**
```json
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
  "distancia_campus_km": 12.3
}
```

**Response:**
```json
{
  "prob_evasao": 0.78,
  "classe_prevista": 1,
  "threshold": 0.5
}
```

### POST `/predict_batch`
Previsão em lote (múltiplos alunos)

**Request Body:**
```json
{
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
      "distancia_campus_km": 12.3
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
      "distancia_campus_km": 5.0
    }
  ]
}
```

**Response:**
```json
{
  "previsoes": [
    {
      "prob_evasao": 0.82,
      "classe_prevista": 1,
      "threshold": 0.5
    },
    {
      "prob_evasao": 0.12,
      "classe_prevista": 0,
      "threshold": 0.5
    }
  ]
}
```

## 💻 Exemplos com cURL

### Health Check
```bash
curl -X GET "http://127.0.0.1:8000/health"
```

### Previsão Individual
```bash
curl -X POST "http://127.0.0.1:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "idade": 19,
    "sexo": "F",
    "tipo_escola_medio": "publica",
    "nota_enem": 650.5,
    "renda_familiar": 2500.0,
    "trabalha": 1,
    "horas_trabalho_semana": 30,
    "reprovacoes_1_sem": 2,
    "bolsista": 0,
    "distancia_campus_km": 12.3
  }'
```

### Previsão em Lote
```bash
curl -X POST "http://127.0.0.1:8000/predict_batch" \
  -H "Content-Type: application/json" \
  -d '{
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
        "distancia_campus_km": 12.3
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
        "distancia_campus_km": 5.0
      }
    ]
  }'
```

## 🧪 Modelo de ML

- **Algoritmo**: Regressão Logística
- **Pipeline**: StandardScaler + OneHotEncoder + LogisticRegression
- **Arquivo**: `model/logistic_model.pkl`
- **Threshold**: 0.5 (configurável em `app/core/config.py`)

## 🛠️ Tecnologias

- **FastAPI**: Framework web moderno e rápido
- **Uvicorn**: Servidor ASGI de alta performance
- **Pydantic**: Validação de dados
- **scikit-learn**: Biblioteca de Machine Learning
- **pandas**: Manipulação de dados
- **joblib**: Serialização de modelos

## 📝 Estrutura do Projeto

```
ml-evasao/
├── app/
│   ├── __init__.py
│   ├── main.py                    # Aplicação FastAPI
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py              # Configurações
│   ├── models/
│   │   ├── __init__.py
│   │   └── student.py             # Entidade de domínio
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── student_schema.py      # Schema de entrada
│   │   └── prediction_schema.py   # Schemas de previsão
│   ├── controllers/
│   │   ├── __init__.py
│   │   └── prediction_controller.py  # Lógica de orquestração
│   ├── services/
│   │   ├── __init__.py
│   │   └── ml_service.py          # Serviço de ML
│   └── views/
│       ├── __init__.py
│       └── prediction_view.py     # Rotas da API
├── model/
│   └── logistic_model.pkl         # Modelo treinado
├── data/
│   └── alunos.csv                 # Dataset (opcional)
├── requirements.txt               # Dependências
└── README.md                      # Este arquivo
```

## 📊 Interpretação dos Resultados

- **prob_evasao**: Probabilidade de evasão (0.0 a 1.0)
  - Próximo de 0: Baixo risco de evasão
  - Próximo de 1: Alto risco de evasão

- **classe_prevista**: 
  - 0: Aluno provavelmente **permanecerá**
  - 1: Aluno provavelmente **evadirá**

- **threshold**: Valor usado para classificação (padrão: 0.5)

## 🤝 Contribuindo

Sinta-se à vontade para contribuir com melhorias!

## 📄 Licença

Este projeto é de código aberto para fins educacionais.

---

Desenvolvido com ❤️ usando FastAPI e scikit-learn
