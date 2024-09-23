# Criando a lista de numeros
my_list = [3, 5, 6, 8, 4, 10, 7, 1, 5, 3]
for iter_var in range(len(my_list)):
    my_list.append(my_list[iter_var] * 2)
print(my_list)
