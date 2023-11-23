from fastapi import APIRouter, status
from classes import Presidente, item, gabinete, User, salvar, consultar, ver, html
rotas = APIRouter()
from fastapi.responses import HTMLResponse


#inventario(create, read, delete)

@rotas.get('/', tags = ["Home"], description="por quenquanto num é nada não kkkkkkkkk")
def home():
    return HTMLResponse(content = html('home'))

@rotas.get("/inventario",tags=["User"], summary="Consultar usuários", description="Recebe 1 parametro do tipo string para realizar a consulta de todos os usuários cadastrados")
async def curiar(tabela: str, coluna: str, busca: str):
    return consultar(tabela, coluna, busca)

@rotas.get("/inventario",tags=["User"], summary="Consultar usuário", description="Recebe 3 parametros do tipo string para realizar a consulta de um único usuário no banco de dados, chama a função de consulta e retorna os dados")
async def curiar(tabela: str, coluna: str, busca: str):
    return consultar(tabela, coluna, busca)

@rotas.post("/newuser", tags=["User"], summary="Cadastrar usuário", description="Recebe informações obrigatórias, no padrão da classe User, e cria um registro no banco de dados")
async def criar_usuario(usuario: User):
    return salvar('user', usuario.dict())

@rotas.delete("/inventario", tags=["User"], summary="Deletar usuário(s)", description="Recebe os parametros de tabela, coluna e o que pesquisar, encontra no banco e faz a remoção")
async def deletar_usuario(tabela: str, coluna: str, busca: str):
    return remover(tabela, coluna, busca)