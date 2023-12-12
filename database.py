import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db_presidentinhos.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME


def criacao_tabelas():
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
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT UNIQUE, 
                            senha TEXT,
                            saldo INTEGER
                            );'''
    Tabelas = [tb_presidente, tb_user]
    for tabela in Tabelas:
        conecta_tudo(tabela)


def conecta_tudo(comando):
    with sqlite3.connect(DB_FILE) as connection:
        cursor = connection.cursor()
        
        cursor.execute(comando)

        if "SELECT" in comando:
            resultado = cursor.fetchall()
            return resultado
        else:
            connection.commit()


def criar_user(carga):
    new_user = f"""INSERT INTO user(nome, senha, saldo)
                    VALUES
                    ('{carga.nome}', '{carga.senha}', {carga.saldo});"""
    return conecta_tudo(new_user)

def listar_usuarios():
    usuarios = """SELECT * FROM user;"""
    return conecta_tudo(usuarios)

def lista_user(nome: str):
    usuario = f"""SELECT * FROM user
                    WHERE nome = '{nome}';"""
    return conecta_tudo(usuario)

def update_saldo(valor: float, user: str):
    atualizacao = f"""UPDATE user
                    SET saldo = {valor}
                    WHERE nome = '{user}';"""
    return conecta_tudo(atualizacao)

def deletar_user(usuario: str):
    lixo = f"""DELETE from user
                where nome = '{usuario}';"""
    return conecta_tudo(lixo)


def criar_presidente(carga):
    nome = "iriri"
    apelido =" "
    new_presida = """INSERT INTO presidente(chave, nome, apelido, vida_max, vida, energia_maxima, energia, rendimento)
                    VALUES
                    ();"""