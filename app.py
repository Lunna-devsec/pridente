from tinydb import TinyDB, Query

# Crie ou abra um banco de dados chamado 'db.json'

def inicializar_db():

    db = TinyDB('db.json')

    pessoas = db.table('pessoas')

    # Consulte dados usando a classe Query
    q = Query()
    resultado = pessoas.search(q.nome == 'bolsonaro')
    print(resultado)


db = TinyDB('db.json')

pessoas = db.table('pessoas')
pessoas.insert({'nome': 'lula', 'rendimento': 100})
pessoas.insert({'nome': 'bolsonaro', 'rendimento': 120})
pessoas.insert({'nome': 'dilma', 'rendimento': 60})
pessoas.insert({'nome': 'Lua', 'rendimento': 1000})


