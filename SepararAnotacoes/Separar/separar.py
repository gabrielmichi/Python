import csv

lista = [] # 1 matriz multidimensional

def ler_arquivo(arquivo):
    #arquivo = '/home/gabriel/PycharmProjects/Separar/teste1.csv'
    with open(arquivo, newline='') as csvfile:
        readarquivo = csv.reader(csvfile, delimiter=';')

        for linha in readarquivo:
            print(lista[1][1])
            lista.append(linha)

        ler_arquivo('/home/gabriel/PycharmProjects/Separar/teste1.csv')
        #for linha in readarquivo:
            #lista.append(linha)

# o módulo csv detectará novas linhas automaticamente
#print(lisa[0][3])



            #gravarquivo = open("gravar.txt", "w")
            #gravarquivo.writelines(lista[0][3])
            #gravarquivo.write('gravando arquivo')
            #gravarquivo.writelines(lista[0][0])

#print(len(lista)) #quantos elementos possui na lista
#print(len(lista2))
#print(lista[0]) # linha 1

#print(lista[1])  linha 2
#print(lista[2])