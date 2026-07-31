class Ordem:
    def __init__(self, id_ordem=None, id_equipamento=None,
    diagnostico="", status="Em andamento", solucao="", data_abertura=None, prioridade="",
    valor_servico=0.0, valor_pecas=0.0, valor_total=0.0, desconto=0.0,observacoes=""):
        self.id_ordem = id_ordem
        self.id_equipamento = id_equipamento
        self.diagnostico = diagnostico
        self.status = status
        self.solucao = solucao
        self.data_abertura = data_abertura
        self.prioridade = prioridade
        self.valor_servico = valor_servico
        self.valor_pecas = valor_pecas
        self.valor_total = valor_total
        self.desconto = desconto
        self.observacoes = observacoes