from src.models import cliente
from src.models.cliente import Cliente
from src.repositories.cliente_repository import atualizar, excluir, inserir, listar


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

        
    elif opcao == "0":
    
            print("Sistema encerrado.")
    
            break

    else:
    
            print("Opção inválida!")
            
if __name__ == "__main__":
    main()