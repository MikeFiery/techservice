from src.database.conexao import conectar
from src.models import ordem

def inserir(ordem):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        INSERT INTO ordem_de_servico (id_equipamento, diagnostico, status, solucao, prioridade,
                           valor_servico, valor_pecas, valor_total, desconto, observacoes)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """


    valores = (
        ordem.id_equipamento,
        ordem.diagnostico,
        ordem.status,
        ordem.solucao,
        ordem.prioridade,
        ordem.valor_servico,
        ordem.valor_pecas,
        ordem.valor_total,
        ordem.desconto,
        ordem.observacoes
    )
    
    cursor.execute(sql, valores)
    conexao.commit()
    ordem.id_ordem = cursor.lastrowid

    cursor.close()
    conexao.close()
    return ordem