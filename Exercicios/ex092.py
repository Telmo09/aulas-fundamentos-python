'''
Crie uma classe Produto com os atributos nome e quantidade em stock.
Adicione um método que mostre o stock no estilo “O produto X tem Y unidades em stock”.
Adicione um novo método que aumenta a quantidade de stock numa determinada quantidade.
'''

class Produto:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

    def stock(self):
        print(f'\nO produto {ProdutoA.nome} tem {ProdutoA.quantidade} unidades em stock\n')

    def alterar(self, mudanca):
        tempquantidade = self.quantidade
        self.quantidade += mudanca
        if tempquantidade > self.quantidade:
            print(f'\nA quantidade de Stock foi reduzida de {tempquantidade} para {self.quantidade}\n')
        if tempquantidade < self.quantidade:
            print(f'\nA quantidade de Stock foi aumentada de {tempquantidade} para {self.quantidade}\n')

ProdutoA = Produto('Coca-Cola', 35)

def start():
    while True:
        print('--- MENU ---')
        print('[1] - Stock da Coca-Cola')
        print('[2] - Alterar Stock')
        print('[3] - Sair')
        opcao = int(input('Selecione uma opçao: '))

        if opcao == 1:
            Produto.stock(ProdutoA)
        elif opcao == 2:
            mudanca = int(input('Indique a quantidade a mudar: '))
            Produto.alterar(ProdutoA, mudanca)
        elif opcao == 3:
            break
        else:
            print('Opcao Invalida !')

start()