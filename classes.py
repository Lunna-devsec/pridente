from pydantic import BaseModel
from typing import List, Optional
from pandas import DataFrame as df
import json



class Presidente(BaseModel):
	chave: str
	nome: str
	rendimento: float 
	tipo: List[str]

class item(BaseModel):
	nome: str 
	recover: int 
	price: float 
	quantidade: int 



class gabinete(BaseModel):
	bandeira: Optional[str] 
	vagas: int
	rendimentos: float
	level: int


class User(BaseModel):
	nome: str
	senha: str 
	saldo: float
	#foto: Optional[str]