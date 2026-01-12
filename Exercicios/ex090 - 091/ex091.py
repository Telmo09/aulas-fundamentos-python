'''
Adicione um método à classe desenvolvida no exercício anterior Livro que imprime
uma descrição do livro no formato:

“O livro com o titulo X foi escrito pelo autor Y".
'''

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

book1 = Livro('A Grande Ilusao', 'Margarida Rebelo Pinto')
book2 = Livro('Portugal e o Segredo de Colombo', 'Manuel da Silva Rosa')
book3 = Livro('Pensar em Grande, Faz Agora', 'Tocha e José Serra')

def start():
    while True:
        print('[ Livro 1 ] : A Grande Ilusao')
        print('[ Livro 2 ] : Portugal e o Segredo de Colombo')
        print('[ Livro 3 ] : Pensar em Grande, Faz Agora')
        print('0 - Sair')
        escolha = int(input('Indique um livro : '))
        if escolha == 1:
            print(f'O livro com o titulo {book1.titulo} foi escrito pelo autor {book1.autor}')
        if escolha == 2:
            print(f'O livro com o titulo {book2.titulo} foi escrito pelo autor {book2.autor}')
        if escolha == 3:
            print(f'O livro com o titulo {book3.titulo} foi escrito pelo autor {book3.autor}')
        if escolha == 0:
            break
        else:
            print('Opção Invalida !')

start()