import sqlite3
from usuario import Usuario
from usuario import Bolsista
from usuario import Analista

class BolsistaDAO:

    def __init__(self, banco):
        self.conn = sqlite3.connect(banco)
        self.cursor = self.conn.cursor()
        self.cursor.execute ("CREATE TABLE IF NOT EXISTS bolsistas (nome TEXT, login TEXT , senha TEXT)")
        self.conn.commit()

    def inserir (self, bolsistas):
        self.cursor.execute (
        "INSERT INTO bolsistas (nome ,login,senha) VALUES (?,?,?)" , (
        bolsistas.nome, bolsistas.login, bolsistas.senha) )
        self.conn.commit()





