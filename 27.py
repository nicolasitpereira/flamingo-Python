print(" [ 1 ] SOMA \n [ 2 ] SUBTRAÇÃO \n [ 3 ] MULTIPLICAÇÃO \n [ 4 ] DIVISÃO \n [ 5 ] EXPONENCIAÇÃO \n [ 6 ] SAIR")
option = int(input("SUA OPÇÃO : "))


while option != 7:
    match option:
        case 1:
            print("SOMA")
            numero1 = float(input("Digite o primeiro numero : "))
            numero2 = float(input("DIgite outro numero : "))
            resultado = numero1 + numero2
            print(f"O resultado da soma é : {resultado}")
            break
        case 2:
            print("SUBTRAIR")
            numero1 = float(input("Digite o primeiro nmumero : "))
            numero2 = float(input("DIgite outro numero : "))
            resultado = numero1 - numero2
            print(f"O resultado da SUBTRAÇÃO é : {resultado}")
            break
        case 3:
            print("MULTIPLICAÇÃO")
            numero1 = float(input("Digite p primeiro numero : "))
            numero2 = float(input("Digite outro numero : "))
            resultado = numero1 * numero2
            print(f"O reesultado da MULTIPLICAÇÃO é : {resultado}")
            break
        case 4:
            print("DIVISÃO")
            numero1 = float(input("Digite p primeiro numero :"))
            numero2 = float(input("Digite outro numero : "))
            resultado = numero1 / numero2
            print(f"O reesultado da DIVISÃO é : {resultado}")
            break
        case 5:
            print("EXPONENCIAÇÃO")
            numero1 = float(input("Digite o primeiro numero : "))
            numero2 = float(input("Digite outro numero : "))
            resultado = numero1 ** numero2
            print(f"O resultado da EXPONENCIAÇÃO é : {resultado}")
            break
        case 6:
            print("SAINDO . . .")
            break

