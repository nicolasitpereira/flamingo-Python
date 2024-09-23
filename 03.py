# criando uma lista de numeros
numbers = [10, 8, 2, 6, 1, 9]

# Variavel para armazenar a soma
sum = 0

# Usando loop for para iterar sobre a lista
for num in range(len(numbers)):
    sum = sum + numbers[num] ** 2
print('A soma vale: {:.2f}'.format(sum))
