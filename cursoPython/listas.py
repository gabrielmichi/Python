#Listas

cidades = ['Rio de Janeiro', 'São Paulo', 'Salvador', 'Goiania']
	#                0		        1		    2	    3

#cidades[0] = 'Brasilia' #altera registro da posição X

print(cidades[0]) #esquerda para direita
print(cidades[-1]) #direita para esquerda

########## Funções em listas ##########

#Documentacao de estrutura de dados
#https://docs.python.org/3/tutorial/datastructures.html

cidades.append('Santa Catarina') #insere registro no final da lista
cidades.remove('Salvador')
cidades.insert('1', 'Pinhalzinho') #insere em determinada posição
cidades.pop(0) #retira da lista a posição X
cidades.sort() #ordena a lista

print(cidades)

########## concatenar listas ##########

numeros = [2,3,4,5]
letras = ['a','b','c','d']

final = numeros + letras
#numeros.extend(letras)

#final = numeros * 4
print(final)

#sublistas
#pos.lista  	  0			            1
itens = [ ['item1', 'item2'], ['item3', 'item4']]
#Pos.item     0	        1	       0	   1

print(itens[1])
print(itens[0][1]) #imprimir primeiro item da segunda lista

########## extrair variaveis com menos código ##########

cidades = ['Rio de Janeiro', 'São Paulo', 'Salvador', 'Goiania', 4, 5]

item1, item2, item3, *outros = cidades
#item1, item2, *outros, item5 = cidades #podemos colocar o outros no meio da lista

print(item1)
print(item2)
print(item3)
print(outros)


########## Loooping dentro da lista ##########
valores = [50, 80, 110, 150, 170]

for x in valores:
	print(f' O valor final do produto é de R${x}.')


########## Validação em listas ##########
cor_cliente = input('Digite a cor desejada: ')
cores = ['amarelo', 'verde', 'azul', 'vermelho']

if cor_cliente.lower() in cores:
	print('Temos essa cor em estoque')
else:
	print('Não temos essa cor em estoque')


########## Agregando listas ##########

#cria uma lista, separando cada caracter na lista
var = list('comprar')

#juntar listas diferentes, concatenando valores
cores = ['amarelo','verde', 'azul', 'vermelho']
valores = [10,20,30,40]

duas_listas = zip(cores,valores)
print(list(duas_listas))

########## Criar lista a partir do input ##########

frutas_usuario = input('Digite o nome das frutas separados por vírgula: ')
frutas_lista = frutas_usuario.split(', ')
print(frutas_lista)