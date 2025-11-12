from datetime import datetime
from sensor import Sensor

class Leitura(Sensor):
    def __init__(self, valor, sensor, timestamp=None):
        super().__init__(sensor.id, sensor.tipo, sensor.unidade, sensor.localizacao)
        self.valor = valor
        if timestamp is None:
            self.timestamp = datetime.now()
        else:
            self.timestamp = timestamp

    def to_dict(self):
        dados = { 'valor': self.valor,
                  'sensor_id': self.id,
                  'sensor_tipo': self.tipo,
                  'timestamp': self.timestamp }
        return dados

    def __str__(self):
        horario = self.timestamp.strftime("%H:%M:%S")

        return f"[{horario}] ID: {self.id} | Tipo: {self.tipo} | Local: {self.localizacao} | Dados: {self.valor:.2f} {self.unidade}"