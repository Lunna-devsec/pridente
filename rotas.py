from fastapi import APIRouter
from classes import Presidente, item, gabinete, User
rotas = APIRouter()



@rotas.get('/')
def home():
    return 'eu estou funcionando'