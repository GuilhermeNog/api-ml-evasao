# 🧪 Comandos para Testar a API

## 📌 Importante
No Windows PowerShell, use os comandos **PowerShell** (recomendado) ou instale curl nativo.

---

## 1️⃣ Testar Raiz da API

### PowerShell
```powershell
Invoke-WebRequest -Uri "http://127.0.0.1:8000/" -Method GET | Select-Object -ExpandProperty Content
```

### cURL (se disponível)
```bash
curl http://127.0.0.1:8000/
```

**Resposta Esperada:**
```json
{
  "message": "API de Previsão de Evasão - OK",
  "version": "1.0.0",
  "docs": "/docs"
}
```

---

## 2️⃣ Health Check

### PowerShell
```powershell
Invoke-WebRequest -Uri "http://127.0.0.1:8000/health" -Method GET | Select-Object -ExpandProperty Content
```

### cURL
```bash
curl http://127.0.0.1:8000/health
```

**Resposta Esperada:**
```json
{
  "status": "ok",
  "model_loaded": true
}
```

---

## 3️⃣ Previsão Individual (POST /predict)

### PowerShell (Opção 1 - Usando arquivo JSON)
```powershell
Invoke-WebRequest -Uri "http://127.0.0.1:8000/predict" -Method POST -ContentType "application/json" -InFile "test_request.json" | Select-Object -ExpandProperty Content
```

### PowerShell (Opção 2 - JSON inline)
```powershell
$body = @'
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
'@

Invoke-WebRequest -Uri "http://127.0.0.1:8000/predict" -Method POST -ContentType "application/json" -Body $body | Select-Object -ExpandProperty Content
```

### cURL (Linux/Mac ou Git Bash no Windows)
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

**Resposta Esperada:**
```json
{
  "prob_evasao": 0.5401831865310669,
  "classe_prevista": 1,
  "threshold": 0.5
}
```

---

## 4️⃣ Previsão em Lote (POST /predict_batch)

### PowerShell (Opção 1 - Usando arquivo JSON)
Primeiro crie o arquivo `test_batch.json` (veja abaixo), depois:
```powershell
Invoke-WebRequest -Uri "http://127.0.0.1:8000/predict_batch" -Method POST -ContentType "application/json" -InFile "test_batch.json" | Select-Object -ExpandProperty Content
```

### PowerShell (Opção 2 - JSON inline)
```powershell
$body = @'
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
'@

Invoke-WebRequest -Uri "http://127.0.0.1:8000/predict_batch" -Method POST -ContentType "application/json" -Body $body | Select-Object -ExpandProperty Content
```

### cURL (Linux/Mac ou Git Bash)
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

**Resposta Esperada:**
```json
{
  "previsoes": [
    {
      "prob_evasao": 0.54,
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

---

## 🎯 Casos de Teste Adicionais

### Aluno com BAIXO risco de evasão
```powershell
$body = @'
{
  "idade": 20,
  "sexo": "M",
  "tipo_escola_medio": "privada",
  "nota_enem": 800.0,
  "renda_familiar": 8000.0,
  "trabalha": 0,
  "horas_trabalho_semana": 0,
  "reprovacoes_1_sem": 0,
  "bolsista": 1,
  "distancia_campus_km": 3.0
}
'@

Invoke-WebRequest -Uri "http://127.0.0.1:8000/predict" -Method POST -ContentType "application/json" -Body $body | Select-Object -ExpandProperty Content
```

### Aluno com ALTO risco de evasão
```powershell
$body = @'
{
  "idade": 25,
  "sexo": "F",
  "tipo_escola_medio": "publica",
  "nota_enem": 450.0,
  "renda_familiar": 1200.0,
  "trabalha": 1,
  "horas_trabalho_semana": 44,
  "reprovacoes_1_sem": 3,
  "bolsista": 0,
  "distancia_campus_km": 50.0
}
'@

Invoke-WebRequest -Uri "http://127.0.0.1:8000/predict" -Method POST -ContentType "application/json" -Body $body | Select-Object -ExpandProperty Content
```

---

## 📝 Formato Bonito da Resposta (PowerShell)

Para ver a resposta formatada de forma legível:

```powershell
(Invoke-WebRequest -Uri "http://127.0.0.1:8000/health" -Method GET).Content | ConvertFrom-Json | ConvertTo-Json -Depth 10
```

Ou para predictions:

```powershell
$body = '{"idade": 19, "sexo": "F", "tipo_escola_medio": "publica", "nota_enem": 650.5, "renda_familiar": 2500.0, "trabalha": 1, "horas_trabalho_semana": 30, "reprovacoes_1_sem": 2, "bolsista": 0, "distancia_campus_km": 12.3}'

(Invoke-WebRequest -Uri "http://127.0.0.1:8000/predict" -Method POST -ContentType "application/json" -Body $body).Content | ConvertFrom-Json | ConvertTo-Json -Depth 10
```

---

## 🚀 Dica Rápida

**Teste mais fácil**: Use o Swagger UI em **http://127.0.0.1:8000/docs** 

Lá você pode testar todos os endpoints com interface visual! 🎨
