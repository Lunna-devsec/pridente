
from fastapi import FastAPI
import uvicorn
from rotas import rotas
from view import html
from classes import gerar

prototipo = FastAPI()
prototipo.include_router(rotas)
prototipo.include_router(html)




import subprocess
def start_server():
    command = [
        "uvicorn",
        "test:prototipo",
        "--host", "localhost",
        "--port", "7777",
        "--reload"
    ]
    
    subprocess.run(command)
if __name__ == "__main__":
    start_server()

