from rotas import rotas
from fastapi import FastAPI
import uvicorn

prototipo = FastAPI()
prototipo.include_router(rotas)


uvicorn.run(prototipo, port = 7777, host = 'localhost')