# Erros
	# Excelente para testes
	# Não realiza o "stop" no programa
	# Mensagens customizadas quando encontra um erro

try:
	letras = ['a', 'b', 'c']
except IndexError:
	print('Index não existe')

### Trabalhando com input
try:
	valor = int(input('Digite o valor do seu produto: '))
	print(valor)
except ValueError:
	print('Favor digitar um valor numérico')

### Utilizando Finally e else

try:
	valor = int(input('Digite o valor do seu produto: '))
	print(valor)
except ValueError:
	print('Favor digitar um valor numérico')
else:
    print('Usuário digitou um valor correto')
    resultado = valor * 2
    print(resultado)
    
## Com o finally, o código posterior sempre será executado depois do except
try:
	valor = int(input('Digite o valor do seu produto: '))
	print(valor)
except ValueError:
	print('Favor digitar um valor numérico')
finally:
    print('Código ok')