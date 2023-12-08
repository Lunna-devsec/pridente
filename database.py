import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db_presidentinhos.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME



tb_presidente = '''CREATE TABLE IF NOT EXISTS presidente(
                        chave TEXT PRIMARY KEY,
                        nome TEXT, 
                        apelido TEXT,
                        vida_max INTEGER,
                        vida INTEGER,
                        energia_max INTEGER,
                        energia INTEGER,
                        rendimento REAL
                        );'''

tb_user = '''CREATE TABLE IF NOT EXISTS user(
                        id INTEGER UNIQUE,
                        nome TEXT PRIMARY KEY, 
                        senha TEXT,
                        saldo INTEGER
                        );'''



def criar_presidente(carga):
    nome = "iriri"
    apelido =" "
    new_presida = """INSERT INTO presidente(chave, nome, apelido, vida_max, vida, energia_maxima, energia, rendimento)
                    VALUES
                    ();"""


def criar_user(carga):
    new_user = f"""INSERT INTO user(nome, senha, saldo)
                    VALUES
                    ('{carga.nome}', '{carga.senha}', {carga.saldo});"""

    with sqlite3.connect(DB_FILE) as connection:
        cursor = connection.cursor()
        
        cursor.execute(tb_user)
        cursor.execute(new_user)
        connection.commit()

def listar_usuarios():
    usuarios = """SELECT * FROM user;"""

    with sqlite3.connect(DB_FILE) as connection:
        cursor = connection.cursor()

        cursor.execute(usuarios)
        resultado = cursor.fetchall()
    return resultado

def lista_user(nome: str):
    usuario = f"""SELECT * FROM user
                    WHERE nome = '{nome}';"""

    with sqlite3.connect(DB_FILE) as connection:
        cursor = connection.cursor()

        cursor.execute(usuario)
        resultado = cursor.fetchall()
    return resultado

def update_saldo(valor: float, user: str):
    atualizacao = f"""UPDATE user
                    SET saldo = {valor}
                    WHERE nome = '{user}';"""

    with sqlite3.connect(DB_FILE) as connection:
        cursor = connection.cursor()

        cursor.execute(atualizacao)
        connection.commit()

def deletar_user(usuario: str):
    lixo = f"""DELETE from user
                where nome = '{usuario}';"""

    with sqlite3.connect(DB_FILE) as connection:
        cursor = connection.cursor()

        cursor.execute(lixo)
        connection.commit()