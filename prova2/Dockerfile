# Use a imagem oficial do Python como base
FROM python:3.8-slim

# Configuração do ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo requirements.txt para dentro do container
COPY requirements.txt .

# Instala as dependências do Python
RUN pip install -r requirements.txt

# Copia o arquivo main.py para dentro do container
COPY main.py .

# Expõe a porta em que o aplicativo FastAPI estará em execução
EXPOSE 8000

# Comando para iniciar o aplicativo usando uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


