class Equipamento:

    def __init__(self, tipo, marca, modelo, numero_serie, id_equipamento=None):
        self.id_equipamento = id_equipamento
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.numero_serie = numero_serie

    def get_tipo(self):
        return self.tipo

    def get_marca(self):
        return self.marca

    def get_modelo(self):
        return self.modelo

    def get_numero_serie(self):
        return self.numero_serie
        return self.telefone

    def get_id_equipamento(self):
        return self.id_equipamento

    def set_tipo(self, tipo):
        self.tipo = tipo

    def set_marca(self, marca):
        self.marca = marca

    def set_modelo(self, modelo):
        self.modelo = modelo

    def set_numero_serie(self, numero_serie):
        self.numero_serie = numero_serie