'''
Crie uma classe chamada Livro que tenha os atributos:
- titulo,
- ano,
- autor
- disponibilidade.
Utilize getters e setters para manipular as propriedades.
'''

class Livro:
    def __init__(self):
        self.__titulo = 'titulo'
        self.__ano = 'ano'
        self.__autor = 'autor'
        self.__disponibilidade = 'disponibilidade'

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, novo_titulo):
        self.__titulo = novo_titulo

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, novo_ano):
        self.__ano = novo_ano

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, novo_autor):
        self.__autor == novo_autor
