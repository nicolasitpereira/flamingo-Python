lista = [1,1,2,3,3,3,3,4,4,4,5,6,7,8,8,9,10,10]

user = int(input("Digite um numero entre 1 e 10 : "))

if user in lista:
    print(f"O numero {user} aparece {lista.count(user)} vezes na lista.")
    print(lista)
else:
    print("Numero não encontrado! Tente novamente.")
