from fastapi import APIRouter, status, Depends
from classes import Presidente, item, gabinete, User
import classes
import database as db

rotas = APIRouter()
from fastapi.responses import HTMLResponse




@rotas.get("/users",tags=["User"], summary="Consultar usuários", description="Realiza a consulta de todos os usuários cadastrados")
async def curiar():
    return db.listar_usuarios()

@rotas.get("/profile/{nome}",tags=["User"], summary="Consultar usuário", description="Realiza a consulta de um único usuário no banco de dados, com base no bone de usuário fornecido")
async def curiar(nome: str):
    return db.lista_user(nome)

@rotas.post("/newuser", tags=["User"], summary="Cadastrar usuário", description="Recebe informações obrigatórias, no padrão da classe User, e cria um registro no banco de dados")
async def criar_usuario(usuario: User):
    db.criar_user(usuario)
    return {"mensagem": "criado"}

@rotas.delete("/profile/{nome}", tags=["User"], summary="Deletar usuário", description="Recebe os parametros de tabela, coluna e o que pesquisar, encontra no banco e faz a remoção")
async def deletar_usuario(nome: str):
    db.deletar_user(nome)
    return {"mensagem": "deletado"}

@rotas.patch("/profile/{nome}", tags=["User"], summary="Atualizar saldo",)
async def atualizar_saldo(saldo: int, nome: str):
    db.update_saldo(saldo, nome)
    return {"mensagem": "saldo atualizado"}
