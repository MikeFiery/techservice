from src.database.conexao import conectar
from src.models import equipamento

def inserir2(equipamento):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        INSERT INTO equipamento (tipo, marca, modelo, numero_serie)
        VALUES (%s, %s, %s, %s)
    """
    valores2 = (equipamento.tipo, equipamento.marca, equipamento.modelo, equipamento.numero_serie)

    cursor.execute(sql, valores2)
    conexao.commit()
    equipamento.id_equipamento = cursor.lastrowid

    cursor.close()
    conexao.close()
    return equipamento

def listar(equipamento):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = """
        SELECT id_equipamento, tipo, marca, modelo, numero_serie
        FROM equipamento
        ORDER BY id_equipamento
    """

    cursor.execute(sql)
    equipamento = cursor.fetchall()

    cursor.close()
    conexao.close()
    return equipamento

def atualizar(equipamento):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        UPDATE equipamento
        SET tipo = %s,
            marca = %s,
            modelo = %s,
            numero_serie = %s,
            data_compra = NOW()
        WHERE id_equipamento = %s
    """
    valores = (equipamento.tipo, equipamento.marca, equipamento.modelo, equipamento.numero_serie, equipamento.id_equipamento)

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()

