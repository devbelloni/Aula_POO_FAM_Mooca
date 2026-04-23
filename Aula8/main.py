from connect import Connect
from usuario import Usuario

if __name__ == "__main__":
    db = Connect()

    # Criando 4 usuários usando a nossa classe
    lista = [
        Usuario("José", "marcos@email.com"),
        Usuario("Julia", "julia@email.com"),
        Usuario("Pedro", "pedro@email.com"),
        Usuario("Sofia", "sofia@email.com")
    ]

    # Inserindo no banco
    for p in lista:
        db.inserir(p)
    
    # Alterando o nome do primeiro usuário (ID 1)
    db.alterar(1, "Marcos Editado")

    # Lendo os dados
    print(f"{'ID':<4} | {'NOME':<15} | {'EMAIL'}")
    print("-" * 40)
    for user in db.listar():
        print(f"{user[0]:<4} | {user[1]:<15} | {user[2]}")