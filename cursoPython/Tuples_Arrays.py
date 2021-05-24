######### Tuples #########
#Armazena mais de uma informação em variáveis
#Manter a sequencia dos dados em uma variável
#Não podem ser alterados (Imutable)
#Portanto, não conseguimos adicionar valores na Tuple
#Tuple ocupa um espaço menor de memória que listas

cores_tuple = ('amarelo', 'vermelho', 'verde', 'azul')
print(cores_tuple)


######### Arrays #########
#Bom utilizar para um grande quantidade de itens
#Melhora problemas de performance
#Bem similar a listas
#https://docs.python.org/pt-br/3/library/array.html

from array import array

letras = array('u', ['a', 'b', 'c', 'd'])
numero_i = array('i', [10,20,30,40])
numero_f = array('f', [1.2, 2.4, 3.2])

print(letras)
print(numero_i)
print(numero_f)