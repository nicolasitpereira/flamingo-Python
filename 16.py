cores = ("vermelho","verde","azul","amarelo","verde","laranja","roxo",
         "vermelho-arroxeado","vermelho-alaranjado","amarelo-esverdeado",
         "amarelo-alaranjado","azul-aroxeeado","azul-esverdado")

print(f"2° item da tupla : {cores[1]}")
print(f"7° item da tupla : {cores[6]}")
print(f"5° item da tupla : {cores[4]}")
print(f"4° item da tupla: {cores[3]}")
print(f"9° item da tupla: {cores[8]}")

print("="*10)
user = int(input("Qual item ? "))

print(f"{user}° item da tupla : {cores[user-1]}")
print(f"E esta na posição : {user-1}")
