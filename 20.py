lista = ["BANANA","UVA","MORANGO","PESSEGO","ABACATE"]

print(lista)
print(f"A lista possui {len(lista)} itens")

option = int(input("Digite [1] para Adicionar ou [2] para remover : "))

if option == 2:
    user = input("Digite a fruta que deseja remover : ").strip().upper()
    if user in lista:
        lista.remove(user)
        print(lista)
    else:
        print("Item não encontrado.")
elif option == 1:
    user = input("Digite a fruta que deseja adicionar : ").strip().upper()
    if user in lista:
        print("A lista JA possui esse item.")
        print(lista)
    else:
        lista.append(user)
        print(lista)
else:
    print("Digite uma opção valida! ")
