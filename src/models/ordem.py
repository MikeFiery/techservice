class Ordem:
    def __init__(self, id_ordem=None, id_equipamento=None,
    diagnostico="", status="Em andamento", data_abertura=None, data_fechamento=None,
    defeito="", servico="", valor=0.0):
        self.id_ordem = id_ordem
        self.id_equipamento = id_equipamento
        self.diagnostico = diagnostico
        self.status = status
        self.data_abertura = data_abertura
        self.data_fechamento = data_fechamento
        self.defeito = defeito
        self.servico = servico
        self.valor = valor

