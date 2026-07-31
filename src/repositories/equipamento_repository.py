from src.database.conexao import conectar


def inserir(equipamento):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        INSERT INTO equipamento (id_cliente, tipo, marca, modelo, numero_serie, data_compra)
        VALUES (%s, %s, %s, %s, %s, CURDATE())
    """
    id_cliente = getattr(equipamento, "id_cliente", None) or 1
    valores2 = (
        id_cliente,
        equipamento.tipo,
        equipamento.marca,
        equipamento.modelo,
        equipamento.numero_serie,
    )

    cursor.execute(sql, valores2)
    conexao.commit()
    equipamento.id_equipamento = cursor.lastrowid

    cursor.close()
    conexao.close()
    return equipamento


def listar():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = """
        SELECT id_equipamento, tipo, marca, modelo, numero_serie
        FROM equipamento
        ORDER BY id_equipamento
    """

    cursor.execute(sql)
    equipamentos = cursor.fetchall()

    cursor.close()
    conexao.close()
    return equipamentos


def atualizar(equipamento):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        UPDATE equipamento
        SET tipo = %s,
            marca = %s,
            modelo = %s,
            numero_serie = %s
        WHERE id_equipamento = %s
    """
    valores = (
        equipamento.tipo,
        equipamento.marca,
        equipamento.modelo,
        equipamento.numero_serie,
        equipamento.id_equipamento,
    )

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()

def excluir(equipamento):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        DELETE FROM equipamento
        WHERE id_equipamento = %s
    """
    valores = (equipamento.id_equipamento)

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()