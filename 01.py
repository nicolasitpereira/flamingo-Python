# Criando a lista de numeros
numbers = [10, 8, 2, 6, 1, 9, 4, 5, 7, 3]

# Inicializando uma variavel que armazenará a soma
soma = 0

# Usando loop for para iterar sobre a lista
for num in numbers:
    soma = soma + num ** 2
print('A soma vale: {:.2f}'.format(soma))
