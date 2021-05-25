velocidade = 40

if velocidade > 110:
    print('Acima da velocidade permitida!')
    print('Favor reduzir a sua velocidade')
elif velocidade < 60:
    print('Favor dirigir acima de 80 Km/h')
else:
    print('Velocidade OK!')

print('###########################')
### Logical Operator 

renda_acima_5mil = True
nome_limpo = False

if renda_acima_5mil or nome_limpo:
    print('Financiamento Aprovado')
else:
    print('Financiamento negado')

if renda_acima_5mil and nome_limpo:
    print('Financiamento Aprovado')
else:
    print('Financiamento negado')

### Multiplos Operadores de comparação

valor = 20

# if valor >= 20 and valor < 40: #Forma comum de se escrever
if 20  <= valor < 40:
    print('Produto foi aceito')
else:
    print('Produto não aceito')
