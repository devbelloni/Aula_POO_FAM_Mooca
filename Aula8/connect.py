import sqlite3

class Connect:
    def __init__(self):
        # Cria a conexão e a tabela
        self.banco = sqlite3.connect('aula.db')
        self.cursor = self.banco.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY, nome TEXT, email TEXT)")

    def inserir(self, u):
        self.cursor.execute("INSERT INTO user (nome, email) VALUES (?, ?)", (u.nome, u._email))
        self.banco.commit()

    def alterar(self, id, novo_nome):
        self.cursor.execute("UPDATE user SET nome = ? WHERE id = ?", (novo_nome, id))
        self.banco.commit()

    def listar(self):
        return self.cursor.execute("SELECT * FROM user").fetchall()