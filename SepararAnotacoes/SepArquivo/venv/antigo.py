import csv

lista = [] # 1 matriz multidimensional


    with open('teste1.csv', newline='') as csvfile: # arquivo2 separe por ;
    readarquivo = csv.reader(csvfile, delimiter=';')
    # o módulo csv detectará novas linhas automaticamente
    for linha in readarquivo:
        #assert isinstance(linha, object)
        lista.append(linha)

    gravarquivo = open("gravar.txt", "w")
    #gravaarquivo = csv.reader(gravaarquivo, delimiter=';')
    gravarquivo.writelines(lista[0][0])
    gravarquivo.write(';')


#print(len(lista)) #quantos elementos possui na lista
#print(len(lista2))
#print(lista[0]) # linha 1
#print(lista[1][2])
#print(lista[1]) # linha 2
#print(lista[2])