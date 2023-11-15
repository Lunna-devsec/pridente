from rotas import rotas
from fastapi import FastAPI
import uvicorn
from app import inicializar_db

prototipo = FastAPI()
prototipo.include_router(rotas)


inicializar_db()

uvicorn.run(prototipo, port = 7777, host = 'localhost')

