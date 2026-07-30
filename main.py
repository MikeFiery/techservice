from src.models.cliente import Cliente
from src.repositories.cliente_repository import inserir, listar


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
    print("0 - Sair")


    opcao = input("Escolha uma opção: ")

    if opcao == "1":
      cliente = inserir(cliente)
      print(f"Cliente gravado na base de dados. ID: {cliente.id_cliente}")
      nome = input("Digite o nome do cliente: ")
      email = input("Digite o email do cliente: ")
      telefone = input("Digite o telefone do cliente: ")
    
    elif opcao == "0":
    
            print("Sistema encerrado.")
    
            break

    else:
    
            print("Opção inválida!")
            
if __name__ == "__main__":
    main()