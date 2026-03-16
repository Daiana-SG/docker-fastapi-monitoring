
# Temperature Monitor API - Dockerized Microservice

Este proyecto demuestra la implementación de un microservicio profesional utilizando FastAPI y Redis, enfocado en prácticas de DevOps como contenedores, redes aisladas y persistencia de datos.

## Tecnologías Utilizadas
FastAPI: Framework de Python para la API.
Redis: Base de datos NoSQL para almacenamiento en caché.
Docker & Docker Compose: Containerización y orquestación.

## Arquitectura
El proyecto consta de dos servicios interconectados:
Web-API: Aplicación Python que corre sobre una imagen slim de Debian.
Cache-DB: Instancia de Redis persistente mediante volúmenes de Docker.

## Características de DevOps Implementadas
Seguridad: Uso de usuarios no-root dentro del contenedor.
Redes: Implementación de una red bridge privada para aislar la base de datos del exterior.
Optimización: Dockerfile multi-capa con aprovechamiento de caché.
Persistencia: Volúmenes de Docker para asegurar que los datos no se pierdan al reiniciar contenedores.

## Cómo ejecutar
Clona el repositorio: git clone ...
Levanta el entorno:
docker-compose up -d
Accede a la documentación automática (Swagger) en: http://localhost:8080/docs
