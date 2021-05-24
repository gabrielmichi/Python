### Set (Listas) ###
# Similar a listas
# Evita itens duplicados
# Não utiliza index

list1 = [10, 20 , 30, 40, 50]
list2 = [10, 20 , 60, 70]

num1 = set(list1)
num2 = set(list2)

print(num1 | num2) #Union - une, porém não mostra valores duplicados
print(num1 - num2) #Difference
print(num1 ^ num2) #Symmetric Difference - retira ambos os valores duplicados
print(num1 & num2) #AND - mostra apenas valores duplicados

##Para criar o set direto
s1 = {1, 2, 3, 4, 5, 6}
s1.add(7)
s1.update([7,8,9,10])
s1.remove(10) #remove valores, porém se o valor não existir, ira gerar um erro
s1.discard(9) #descarta o valor, caso não exista, não irá gerar erros
print(s1)

##Sets - trabalhando com strings

set1 = {'a', 'b', 'c'}
set2 = {'a', 'd', 'e'}
set3 = {'c', 'd', 'f'}

set4 = set1.union(set2) #realiza união dos sets
set5 = set1.intersection(set2) #apenas os valores em comum
set6 = set1.symmetric_difference(set3) #retira todos os duplicados

print(set4)