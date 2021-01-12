
class Cliente:

    def __init__(self, nome):
        self.__nome = nome

# Properties
    @property
    def nome(self):
        print("chamando @property nome()")
        # altera primeira letra p/ maiusculo
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        print("chamando setter nome()")
        self.__nome = nome

#from cliente import Cliente