from src.models import cliente
from src.models.cliente import Cliente
from src.repositories.cliente_repository import atualizar, excluir, inserir, listar
from src.models import equipamento
from src.models.equipamento import Equipamento
from src.repositories.equipamento_repository import atualizar, inserir2, listar


def main():
    print("=== TechService - Sistema de Gestão de Assistência Técnica ===")

    cliente = Cliente(
        nome="Cliente Teste",
        email="teste@email.pt",
        telefone="910000000"
    )

while True:

    print("\n=== TechService - Sistema de Gestão de Assistência Técnica ===")

    print("1 - Inserir Clientes")
    print("2 - Listar Clientes")
    print("3 - Editar Clientes")
    print("4 - Excluir Clientes")
    print("5 - Inserir Equipamentos")
    print("6 - Listar Equipamentos")
    print("7 - Editar Equipamentos")
    print("0 - Sair")


    opcao = input("Escolha uma opção: ")

    if opcao == "1":
      
      
      nome = input("Digite o nome do cliente: ")
      email = input("Digite o email do cliente: ")
      telefone = input("Digite o telefone do cliente: ")

      cliente = inserir(Cliente(nome=nome, email=email, telefone=telefone))
      print(f"Cliente gravado na base de dados. ID: {cliente.id_cliente}")

    elif opcao == "2":

        clientes = listar()
        if clientes:
            print("\n=== Lista de Clientes ===")
            for cliente in clientes:
                print(f"ID: {cliente['id_cliente']}, Nome: {cliente['nome']}, Email: {cliente['email']}, Telefone: {cliente['telefone']}")
        else:
            print("Nenhum cliente encontrado.")

    elif opcao == "3":
    
        id_cliente = input("Digite o ID do cliente que deseja editar: ")
        nome = input("Digite o novo nome do cliente: ")
        email = input("Digite o novo email do cliente: ")
        telefone = input("Digite o novo telefone do cliente: ")

        cliente = Cliente(nome=nome, email=email, telefone=telefone, id_cliente=id_cliente)
        atualizar(cliente)
        print(f"Cliente com ID {id_cliente} atualizado com sucesso.")

    elif opcao == "4":
    
        cliente = Cliente(id_cliente=id_cliente)
        excluir(cliente)
        print(f"Cliente com ID {id_cliente} excluído com sucesso.")

    elif opcao == "5":

        tipo = input("Digite o tipo do equipamento: ")
        marca = input("Digite a marca do equipamento: ")
        modelo = input("Digite o modelo do equipamento: ")
        numero_serie = input("Digite o número de série do equipamento: ")

        equipamento = inserir2(Equipamento(tipo=tipo, marca=marca, modelo=modelo, numero_serie=numero_serie))
        print(f"Equipamento gravado na base de dados. ID: {equipamento.id_equipamento}")


    elif opcao == "6":
        equipamentos = listar()
        if equipamentos:
            print("\n=== Lista de Equipamentos ===")
            for equipamento in equipamentos:
                print(f"ID: {equipamento['id_equipamento']}, Tipo: {equipamento['tipo']}, Marca: {equipamento['marca']}, Modelo: {equipamento['modelo']}, Número de Série: {equipamento['numero_serie']}")
        else:
            print("Nenhum equipamento encontrado.")

    elif opcao == "7":
        id_equipamento = input("Digite o ID do equipamento que deseja editar: ")
        tipo = input("Digite o novo tipo do equipamento: ")
        marca = input("Digite a nova marca do equipamento: ")
        modelo = input("Digite o novo modelo do equipamento: ")
        numero_serie = input("Digite o novo número de série do equipamento: ")

        equipamento = Equipamento(tipo=tipo, marca=marca, modelo=modelo, numero_serie=numero_serie, id_equipamento=id_equipamento)
        atualizar(equipamento)
        print(f"Equipamento com ID {id_equipamento} atualizado com sucesso.")
                   
    elif opcao == "0":
    
            print("Sistema encerrado.")
    
            break

    else:
    
            print("Opção inválida!")
            
if __name__ == "__main__":
    main()