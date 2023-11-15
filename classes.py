from pydantic import BaseModel
from typing import List, Optional
from tinydb import TinyDB, Query
aaaaaa

class Presidente(BaseModel):
	chave: str
	nome: str 
	apelido: Optional[str] = None
	vida_max: int = 50
	vida: int 
	energia_max: int = 100 
	energia: int 
	frases: List[str]
	rendimento: float 
	tipo: List[str] 
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
    return 200

def consultar(tabela: str, coluna: str, busca: str):
    with TinyDB('tempdb.json') as db:
        temp = db.table(tabela)
        return temp.search(Query()[coluna] == busca)