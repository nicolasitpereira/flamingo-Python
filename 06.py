frutas = ["pera", "banana", "cereja", "laranja", "kiwi", "melão", "manga"]

user = str(input("Qual fruta? ")).strip().lower()
#metodo strip(): para remover possiveis espaços digitado pelo usuario
#metodo lower(): caso usuario digite letras maiusculas converter para minusculas como esta na lista

if  user in frutas: #o que o usuario digitou esta dentro da lista?
    print('Temos essa fruta.')
else:
    print('Infelizmente não temos essa fruta.')
    add = str(input('Deseja adicionar esta fruta a lista? [S/N] ')).strip().upper()
    # metodo upper(): caso usuario digite letras minusculas converter para maiusculas
    if add == 'S':
        frutas.append(user)
        print(frutas)
    else:
        print('Certo')
        print(frutas)
