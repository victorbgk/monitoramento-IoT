import random

class Sensor:
    
    def __init__(self, id, tipo, unidade, localizacao):
        self.id = id
        self.tipo = tipo
        self.unidade = unidade
        self.localizacao = localizacao

    def gerar_leitura(self):

        valor = 0

        if self.tipo == "temperatura do solo":

            valor = random.uniform(20, 35)

        elif self.tipo == "temperatura do ar":

            valor = random.uniform(20, 35)

        elif self.tipo == "umidade do ar":

            valor = random.uniform(0, 100)

        elif self.tipo == "umidade do solo":

            valor = random.uniform(0, 100)

        elif self.tipo == "salinidade":

            valor = random.uniform(1, 4)

        elif self.tipo == "radiacao solar":

            valor = random.uniform(200, 1000)

        return valor

    def exibir_cadastro(self):

        return f"ID do sensor: {self.id} | tipo de sensor: {self.tipo}"