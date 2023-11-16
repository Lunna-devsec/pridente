from fastapi import APIRouter, status
from classes import Presidente, item, gabinete, User, salvar, consultar
rotas = APIRouter()


#inventario(create, read, delete)

@rotas.get('/', tags = ["Home"])
def home():
    return 'Pesidentinhos'

@rotas.get("/inventario",tags=["User"], summary="Consultar usuário(s)", description="Recebe 3 parametros do tipo string para realizar a consulta no banco de dados, chama a função de consulta e retorna os dados")
async def curiar(tabela: str, coluna: str, busca: str):
    return consultar(tabela, coluna, busca)

@rotas.post("/newuser", tags=["User"], summary="Cadastrar usuário")
async def criar_usuario(usuario: User):
    return salvar('user', usuario.dict())

@rotas.delete("/inventario", tags=["User"], summary="Deletar usuário(s)", description="")
async def deletar_usuario(tabela: str, coluna: str, busca: str):
    return remover(tabela, coluna, busca)