# 1. Base ligera
FROM python:3.11-slim

# 2. Directorio de trabajo
WORKDIR /app

# 3. Instalación de dependencias (Aprovechando el caché de capas)
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copiar código
COPY app/ .

# 5. No correr como root (Seguridad)
RUN useradd -m devopsuser
USER devopsuser

# 6. Comando de ejecución
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
