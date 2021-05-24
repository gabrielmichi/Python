####### List Comprehension #######
# Mais simples de se escrever
# Utilizado quando você precisa criar uma nova lista a partir de uma existente
# [expressao for iten in itens]

frutas1 = ['abacate', 'banana', 'morango', 'kiwi', 'abacaxi']
frutas2 = []

#exemplo 1
#Loop de forma convencional
for iten in frutas1:
    if 'n' in iten:
        frutas2.append(iten)
print(frutas2)

#List comprehension
frutas2 = [iten for iten in frutas1 if 'n' in iten]
print(frutas2)

#exemplo 2
#Loop de forma convencional
valores = []
for x in range(6):
    valores.append(x * 10)

valores = [x * 10 for x in range(6)]
print(valores)

########### Generator Expressions ###########
# Uma forma mais rápida para listas, dicionários etc..
# Menos memória alocada
# Valores em bytes
# A diferença do generator para listas na declaração, é trocar os "[]" por "()"
from sys import getsizeof

numeros = [x * 10 for x in range(1000000)]
print(type(numeros))
print(getsizeof(numeros))

print("############")

numeros = (x * 10 for x in range(1000000))
print(type(numeros))
print(getsizeof(numeros))