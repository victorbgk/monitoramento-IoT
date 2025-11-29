class Usuario:

    def __init__(self, nome, login, senha):
        self.nome = nome
        self.login = login
        self.senha = senha

    def get_login(self):

        return self.login

    def set_login(self, login):

        self.login = login

    def get_senha(self):

        return self.senha

    def set_senha(self, senha):

        self.senha = senha

    def verificar_senha(self, senha):

        if self.senha == senha:

            return True

        else:

            return False

    def cadastrar_sensor(self):

        return False

class Bolsista(Usuario):

    def __init__(self, nome, login, senha):

        super().__init__(nome, login, senha)

    def cadastrar_sensor(self):

        return True

class Analista(Usuario):

    def __init__(self, nome, login, senha):

        super().__init__(nome, login, senha)

    def cadastrar_sensor(self):

        return False