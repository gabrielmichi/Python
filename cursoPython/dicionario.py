######## Dicionários ########
#Utiliza index no formato de Keys e Values
#Aceita string, integer, float, boolean...
#realiza as buscas pela key

aluno = {'nome': 'Ana', 'idade': 16, 'nota_final': 'A', 'aprovacao': True}

print(aluno)
print(aluno['idade'])

aluno['nome'] = 'Jose'
aluno.update({'nome': 'Gabriel', 'nota_final': '8'})
aluno.update({'endereco': 'Rua dos joses'})

del aluno['idade'] #remove key idade

print(aluno)
print(aluno.get('cidade')) #Com o get não gera erros, caso não exista a key
print(aluno.get('cidade', 'nao existe'))

for x in aluno: #Por padrao ele imprime as keys
    print(x)

for x in aluno.values(): #Alteracao para imprimir os valores
    print(x)

for keys, values in aluno.items(): #imprimir ambos
    print(keys, values)


print('################################################################################')

aluno2 = {
    'nome': 'Gabriela', 
    'idade': 17, 
    'nota_final': 'A', 
    'aprovacao': True, 
    'Materias': ['Fisica', 'Matematica', 'Geografia']}
print(aluno2)
print(aluno2.get('Materias'))
print(len(aluno2)) #contar quantidade de valores (keys)

print(aluno2.keys())
print(aluno2.values())
print(aluno2.items()) #traz o dicionario completo