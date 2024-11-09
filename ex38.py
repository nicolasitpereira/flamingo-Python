# Conjuntos aninhados

conjunto_1 = {1, 2, 3}
conjunto_2 = {3, 4, 5}
conjunto_3 = {5, 6, 7}

conjunto_aninhado = {frozenset(conjunto_1), frozenset(conjunto_2), frozenset(conjunto_3)}

uniao_total = set.union(*[set(c) for c in conjunto_aninhado])

print("União dos conjuntos aninhados:", uniao_total)

