from tinydb import TinyDB, Query

# Crie ou abra um banco de dados chamado 'db.json'

def inicializar_db():

    db = TinyDB('db.json')

    pessoas = db.table('pessoas')

    # Consulte dados usando a classe Query
    q = Query()
    resultado = pessoas.search(q.nome == 'bolsonaro')
    print(resultado)




