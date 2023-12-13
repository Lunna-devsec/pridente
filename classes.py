from pydantic import BaseModel
from typing import List, Optional
from random import random as rand
from random import randint as rint



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



class gerar:
	maxrarity = 15
	valor_base = 10
	rendimento_inicial = 5
	quantidade_presidente = 11

	@classmethod
	def raridade(cls, lvl):
		gotcha= rint(1, 100) * (sum(rand() for _ in range(lvl - 1)) + lvl / 2)
		
		raridade = 1
		limite = 80
		while gotcha > limite:
			if raridade == cls.maxrarity:break
			raridade += 1
			limite = 80 + (800 - 80) * (raridade / cls.maxrarity) ** 2
		return raridade
	
	@classmethod
	def valor(cls, raridade):
		def multiplyer(r):
			multi = (1.5 + (0.25 * (r - 2))) * r - 1
			multi = cls.valor_base if r == 1 else cls.valor_base * multi
			return multi
		
		min = raridade - 1
		min = cls.rendimento_inicial if min == 0 else multiplyer(min)
		max = multiplyer(raridade)
		min = int(min)
		max = int(max)

		return rint(min, max)
	
	@classmethod
	def escolher(cls):
		return rint(0, cls.quantidade_presidente - 1)
	
	@classmethod
	def presidente(cls, lvl):
		raridade = cls.raridade(lvl)
		valor = cls.valor(raridade)
		escolher = cls.escolher()
		return {'id': escolher, 'raridade': raridade, 'valor': valor}