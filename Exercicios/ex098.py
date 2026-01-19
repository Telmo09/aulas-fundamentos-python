class Produto:
    def __init__(self, nome, qtd=0):
        self.__nome = nome
        self.__qtd_stock = self.__e_negativo(qtd)

    def __e_negativo(self, valor):
        if valor < 0:
            raise ValueError("A quantidade em stock não pode ser negativa.")
        return valor

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        if not nome:
            raise ValueError("O nome não pode ser vazio.")
        self.__nome = nome

    @property
    def qtd_stock(self):
        return self.__qtd_stock

    @qtd_stock.setter
    def qtd_stock(self, qtd):
        self.__qtd_stock = self.__e_negativo(qtd)

    def mostrar(self):
        return f'{self.__nome}: {self.__qtd_stock} unidades'

    def aumentar_stock(self, valor):
        valor = self.__e_negativo(valor)

batatas = Produto('Batatas', 20)
print(batatas.mostrar())
batatas.qtd_stock += 10
print(batatas.mostrar())