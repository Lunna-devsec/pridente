from fastapi import APIRouter, status
from classes import Presidente, item, gabinete, User, salvar, consultar
rotas = APIRouter()


#inventario(create, read, delete)

@rotas.get('/', tags = ["Home"])
def home():
    return 'Pesidentinhos'

@rotas.get("/inventario",tags=["User"])
async def curiar(tabela: str, coluna: str, busca: str):
    teste = consultar(tabela, coluna, busca)
    return teste

@rotas.post("/newuser", tags=["User"])
async def criar_usuario(usuario: User)
    return salvar('user', usuario.dict())

#@rotas.delete("/")
#async 