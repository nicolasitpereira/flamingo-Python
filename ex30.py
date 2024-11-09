# removendo itens do set

myset = {"NICOLAS", "BRUNA", "TALISSA", "SAMUEL", "GUILHERME"}
print(myset)

option = "S"

while option == "S":
    user = input("Quem deseja remover do Set? ").strip().upper()

    if user not in myset:
        print("Nome Inválido!")
    else:
        myset.remove(user)
        print(f"{user} removido.")

    print("Conjunto atual:", myset)

    option = input("Deseja continuar removendo? [S]/[N] ").strip().upper()

print("Programa encerrado.")
