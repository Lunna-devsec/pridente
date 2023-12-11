from pydantic import BaseModel
from typing import List, Optional
from tinydb import TinyDB, Query
from pandas import DataFrame as df
import json



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
	rendimentos: float





class User(BaseModel):
	nome: str
	senha: str 
	saldo: float
	#foto: Optional[str]





def remover(tabela: str, coluna: str, busca: str):
	with TinyDB('tempdb.json') as db:
		temp = db.table(tabela)
		if consultar(tabela, coluna, busca):
			temp.remove(Query()[coluna] == busca)
			return True
		else:
			return False
from tinydb import TinyDB

def ver(tabela):

    with TinyDB('tempdb.json') as db:
        dados_lista = db.table(tabela).all()
        print(json.dumps(dados_lista, indent=2))
        return dados_lista