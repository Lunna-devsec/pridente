import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db_presidentinhos.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME


def criacao_tabelas():

    tb_user = '''CREATE TABLE IF NOT EXISTS user(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT UNIQUE, 
                            senha TEXT,
                            saldo INTEGER
                            );'''

    tb_tipo = '''CREATE TABLE IF NOT EXISTS tipos(
                            cd_tipo INTEGER PRIMARY KEY,
                            nome TEXT UNIQUE
                            );'''

    tb_gabinete = '''CREATE TABLE IF NOT EXISTS gabinete(
                            id_user INTEGER PRIMARY KEY,
                            vagas INTEGER,
                            rendimentos REAL, 
                            level INTEGER,
                            cd_tipo INTEGER,
                            FOREIGN KEY (cd_tipo) REFERENCES tb_bandeira(cd_tipo)
                            );'''
    
    tb_modelo = '''CREATE TABLE IF NOT EXISTS modelo_presidente(
                            cd_modelo INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT
                            );'''
    
    tb_presidente = '''CREATE TABLE IF NOT EXISTS presidente(
                            id_pres INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT,
                            rendimento REAL,
                            raridade INTEGER,
                            id_user INTEGER,
                            cd_modelo INTEGER,
                            FOREIGN KEY (id_user) REFERENCES tb_user(id),
                            FOREIGN KEY (cd_modelo) REFERENCES modelo_presidente(cd_modelo)
                            );'''

    Tabelas = [tb_presidente, tb_user, tb_modelo]
    for tabela in Tabelas:
        conecta_tudo(tabela)


def cargas():
    carga = """INSERT INTO tb_modelo(cd_modelo, nome)
                VALUES
                (1, 'Lula'),
                (2, 'Bolsonaro'),
                (3, 'Itamar Franco');"""
    conecta_tudo(carga)

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
    new_presida = """INSERT INTO presidente(chave, nome, apelido, vida_max, vida, energia_maxima, energia, rendimento)
                    VALUES
                    ();"""