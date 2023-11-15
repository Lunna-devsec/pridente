from fastapi import APIRouter
from classes import Presidente, item, gabinete, User, salvar
rotas = APIRouter()


#inventario(create, read, delete)

@rotas.get('/')
def home():
    return 'Pesidentinhos'


@rotas.post("/newuser")
async def criar_usuario(usuario: User):
    salvar('user', usuario)
    return usuario

