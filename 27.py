print(" [ 1 ] SOMA \n [ 2 ] SUBTRAÇÃO \n [ 3 ] MULTIPLICAÇÃO \n [ 4 ] DIVISÃO \n [ 6 ] EXPONECIAÇÃO \n [ 7 ] SAIR")
option = int(input("SUA OPÇÃO : "))


while option != 7:
    match option:
        case 1:
            print("SOMA")
            numero1 = int(input("Digite o primeiro nmumero para SOMA : "))
            numero2 = int(input("DIgite outro numero para SOMA : "))
            resultado = numero1 + numero2
            print(f"O resultado da soma é : {resultado}")
            break
        case 2:
            print("SUBTRAIR")
            numero1 = int(input("Digite o primeiro nmumero para SUBTRAIR : "))
            numero2 = int(input("DIgite outro numero para SUBTRAIR : "))
            resultado = numero1 - numero2
            print(f"O resultado da SUBTRAÇÃO é : {resultado}")
            break
