# Verificando SE o Número digitado pelo usuário está presente no conjunto

myset = {1,6,2,8,9,4,67,33,11,51,88}

user = int(input("Digite um Numero : "))

if user in myset:
    print(myset)
    print("O número digitado ESTÁ presente na lista.")
else:
    print(myset)
    print("O número digitado NÃO ESTÁ presente no Conjunto.")
