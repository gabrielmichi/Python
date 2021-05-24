############ Lambda Function ############
# é uma função (pequena) sem nome
# pode ter vários argumentos mas somente 1 expressão
# Muito utilizada dentro de outras funções
# código mais 'clean'

#x é o argumento
somar10 = lambda x: x + 10
somar20 = lambda x,y: x + y + 20
print(somar10(2))
print(somar20(3,5))

print('####################################################')

#Sub-função, utilizando Lambda dentro de outra função
def somar(x):
    func2 = lambda x: x + 10
    return func2(x) * 4

print(somar(2))