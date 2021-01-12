import csv
lista = [] # 1 matriz multidimensional
listaarquivos = []

def ler_arquivo(arquivo):
    arquivo_aberto = open(arquivo, newline='') #as csvfile:
    return csv.reader(arquivo_aberto, delimiter=';') # separe por vírgula

    teste.csv

    gravarquivo = open("gravar.txt", "w")
    # o módulo csv detectará novas linhas automaticamente
    for linha in readarquivo:
        lista.append(linha)
        #lista.append(linha)



#print(lista[0]) # linha 1
#print(lista[1]) # linha 2
#print(lista[2])