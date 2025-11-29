from datetime import datetime

class Leitura:
    def __init__(self, valor, dados_sensor):
        self.valor = valor
        self.dados_sensor = dados_sensor
        self.timestamp = datetime.now()

    def to_dict(self):

        dicionario = {

            'valor': self.valor,
            'sensor_id': self.dados_sensor.id,
            'sensor_tipo': self.dados_sensor.tipo,
            'timestamp': self.timestamp

        }

        return dicionario

    def exibir_leitura(self):

        horario = f"{self.timestamp:%H:%M:%S}"

        return f"ID do sensor: {self.dados_sensor.id} | tipo de sensor: {self.dados_sensor.tipo} | localizacao do sensor: {self.dados_sensor.localizacao} | dados da leitura: {self.valor:.2f} {self.dados_sensor.unidade} [{horario}]"