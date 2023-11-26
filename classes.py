from pydantic import BaseModel
from typing import List, Optional
from tinydb import TinyDB, Query
from pandas import DataFrame as df
from datetime import datetime
import json



class Presidente(BaseModel):
	chave: str
	nome: str 
	apelido: Optional[str] = None
	vida_max: int = 50
	vida: int = vida_max
	energia_max: int = 100 
	energia: int = energia_max
	frases: List[str]
	rendimento: float 
	tipo: List[str] 
	time: str = datetime.now().strftime("%H:%M:%S")
	vivo: bool = True
	

class item(BaseModel):
	nome: str 
	recover: int 
	price: float 
	quantidade: int 



class gabinete(BaseModel):
	bandeira: Optional[str] 
	vagas: int 
	cadeiras: Optional[List[str]]
	rendimentos: float 



class User(BaseModel):
	id: int 
	nome: str 
	senha: str 
	saldo: float 
	foto: Optional[str]



def salvar(tabela: str, jason: dict):
    with TinyDB('tempdb.json') as db:
        temp = db.table(tabela)
        temp.insert(jason)
    return True

def consultar(tabela: str, coluna: str, busca: str):
    with TinyDB('tempdb.json') as db:
        temp = db.table(tabela)
        return temp.search(Query()[coluna] == busca)

def remover(tabela: str, coluna: str, busca: str):
	with TinyDB('tempdb.json') as db:
		temp = db.table(tabela)
		if consultar(tabela, coluna, busca):
			temp.remove(Query()[coluna] == busca)
			return True
		else:
			return False


def add_presidente():
	novo = Presidente(nome = "presidente de teste", chave = "11212", frases = ["sou apenas um teste"], rendimento = 20, tipo = ['testador'])
	novo = novo.dict()
	
	with TinyDB('testers.json') as teste:
		temp = teste.table("presidente")
		temp.insert(novo)
	return True

def ver(tabela):

    with TinyDB('tempdb.json') as db:
        dados_lista = db.table(tabela).all()
        print(json.dumps(dados_lista, indent=2))
        return dados_lista


def html(pagina):
	if pagina == 'home':
		with open('home.html', 'r') as home:
			return home.read()