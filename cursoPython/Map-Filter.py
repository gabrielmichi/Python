####### Map Function #######
# Muito utilizado com listas
# Aplicar uma função a um Iterable, por item. (list, turple, dic etc)

####https://docs.python.org/3/library/functions.html

lista1 = [1, 2, 3, 4]

#Função Map em uma lista
def multi(x):
    return x * 2
lista2 = map(multi, lista1)
print(list(lista2))

### MAP com Lambda
### Com 1 linha, conseguimos substituir as 4 do exemplo anterior
print(list(map(lambda x: x*2, lista1)))

###### FILTER ######

valores = [10, 12, 40, 45, 57]

def remover20(x):
    return x > 20
print(list(filter(remover20, valores)))

## mesmo exemplo, utilizando lambda
print(list(filter(lambda x: x > 20, valores)))