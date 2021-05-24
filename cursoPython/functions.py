#funcoes de calculo

def somar_dois_numeros():
    numero1 = 10
    numero2 = 5
    resultado = numero1 + numero2
    print(resultado)
somar_dois_numeros()

#funcoes com argumentos na entrada
def boas_vindas(nome,quantidade):
    print(f'Olá {nome}.')
    print(f'Temos {str(quantidade)} laptops em estoque')
boas_vindas('Gabriel', 10)
boas_vindas('José', 5)
boas_vindas('Alberto', 20)

#Funcoes com argumentos "Default" e "Non-default"
def boas_vindas(nome,quantidade=6):
    print(f'Olá {nome}.')
    print(f'Temos {str(quantidade)} laptops em estoque')

######## PRINT OR RETURN ########
#Realizam uma tarefa
#Calcula e retorna um valor
#Print irá apenas mostrar o valor
#return armazena o valor que poderá ser mostrado depois


######## Varios argumentos Xargs ########
def soma(*numeros):
    resultado = 0
    for num in numeros:
        resultado += num    
    return resultado

x = soma(2,3,4,5)
print(x)

##Os 2 ** significa que pode passar vários argumentos e varios parâmetros
def agencia(**carro):
    return carro

print(agencia(marca='Gol', cor='Branca', motor=1.0, placa='FGG-2932'))
print(agencia(marca='Civic', cor='Preto', placa='FGG-2932'))
