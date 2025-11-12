class Usuario:
    def __init__(self, nome, login, senha):
        self.nome = nome
        self.__login = login
        self.__senha = senha

    def get_login(self):
        return self.__login

    def set_login(self, login):
        self.__login = login

    def get_senha(self):
        return self.__senha

    def set_senha(self, senha):
        self.__senha = senha

    def verificar_senha(self, senha):
        if self.__senha == senha:
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
