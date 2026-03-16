import os
import redis
from fastapi import FastAPI

app = FastAPI()

# Configuración por variables de entorno (Práctica Profesional)
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = os.getenv("REDIS_PORT", 6379)

# Conexión a la DB
db = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

@app.get("/")
def home():
    return {"status": "Online", "service": "Temperature Monitor"}

@app.get("/log/{temp}")
def log_temp(temp: float):
    db.set("last_temp", temp)
    return {"message": f"Temperatura {temp} guardada en Redis."}

@app.get("/get-temp")
def get_temp():
    last_temp = db.get("last_temp")
    return {"last_temp": last_temp if last_temp else "No hay datos"}
