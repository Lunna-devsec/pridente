from fastapi import APIRouter, status, Depends
from classes import Presidente, item, gabinete, User
import classes
import database as db

rotas = APIRouter()
from fastapi.responses import HTMLResponse

#inventario(create, read, delete)

@rotas.get('/', tags = ["Home"], description="renderiza a pagina home")
def home():
    return HTMLResponse(content = html('home'))

#@rotas.post("/teste")
#async def criar_user(user: classes.User, db: Session = Depends(get_db)):
#    novo_user = RUser(db).criar(user)
#    return novo_user
@rotas.get("/users",tags=["User"], summary="Consultar usuários", description="Realiza a consulta de todos os usuários cadastrados")
async def curiar():
    db.listar_usuarios()
    return {"mensagem": "aaaaaa"}

#@rotas.get("/inventario",tags=["User"], summary="Consultar usuário", description="Realiza a consulta de um único usuário no banco de dados, com base no bone de usuário fornecido")
#async def curiar(tabela: str, coluna: str, busca: str):
#    return consultar(tabela, coluna, busca)

@rotas.post("/newuser", tags=["User"], summary="Cadastrar usuário", description="Recebe informações obrigatórias, no padrão da classe User, e cria um registro no banco de dados")
async def criar_usuario(usuario: User):
    db.criar_user(usuario)
    return {"mensagem": "criado"}

@rotas.delete("/inventario/{nome}", tags=["User"], summary="Deletar usuário(s)", description="Recebe os parametros de tabela, coluna e o que pesquisar, encontra no banco e faz a remoção")
async def deletar_usuario(nome: str):
    db.deletar_user(nome)
    return {"mensagem": "deletado"}

@rotas.patch("/inventario/{nome}")
async def atualizar_saldo(saldo: int, nome: str):
    db.update_saldo(saldo, nome)
    return {"mensagem": "saldo atualizado"}