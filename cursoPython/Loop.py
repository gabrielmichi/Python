#### For Loops

# Imprimir de 1 a 5
for numero in range(6): #Comeca no 0
    print(numero)
for numero in range(1,6):
    print(numero)

# Trabalhando com Strings
palavra = 'Espetacular'
for letra in palavra:
    print(f'{letra} está na Palavra {palavra}')

# Utilizando If-Else
compra_confirmada = True
dados_compra = 'Compra no valor de R$12,50 e entrega confirmada'

for enviar in range(3):
    if compra_confirmada:
        print(dados_compra)
        print('Detalhes enviados por e-mail!')
        break
    else:
        print('Falha na compra')


print('#####################################################')

#### Nested Loops
# Um loop dentro do outro
# outer loop
# inner loop

for numero1 in range(5):
    print('Produto' + str(numero1))
    for numero2 in range(5):
        print(numero1, numero2)

print('#####################################################')

## Separando Strings
# mODIFICAR de Fantastico para F A N T A S T I C O
palavra = 'FANTASTICO'

for spaco in palavra:
    print(f' {spaco}', end='')

print('##############################################')
#### Gerar um retângulo

linhas = 6
colunas = 6
simbolo = '@'

for l in range(linhas):
    for c in range(colunas):
        print(simbolo, end='')
    print()


print('##############################################')

######### While Loops #########
# Excelente para loops dependentes de uma condição
# Criar uma promoção para um produto no valor de R$100

valor = 100
preco_custo = 20
dia = 0

while valor > preco_custo:
    dia += 1
    print(f' No dia {dia} o produto vai ser vendido por R${valor}')
    valor -= 5

#Adicionar porcentagem no valor final
valor = int(input('Digite o valor do seu produto em R$: '))

while valor > preco_custo:
    valor = (valor * 0.10) + valor
    print(f' O valor final do seu produto será de R${valor}')
    break
    
