# Usa a imagem oficial Python como base
FROM python:3.10-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos necessários
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expõe a porta (ajuste conforme necessário)
EXPOSE 8000

# Comando para iniciar o serviço
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
