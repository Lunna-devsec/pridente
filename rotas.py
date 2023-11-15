from fastapi import APIRouter
rotas = APIRouter()



@rotas.get('/')
def home():
    return 'eu estou funcionando'