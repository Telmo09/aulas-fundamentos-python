'''
Crie uma classe chamada Livro que tenha dois atributos:
- titulo e autor.
Instancie três objeto dessa classe e imprima os valores dos atributos.
'''

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

book1 = Livro('A Grande Ilusao', 'Margarida Rebelo Pinto')
book2 = Livro('Portugal e o Segredo de Colombo', 'Manuel da Silva Rosa')
book3 = Livro('Pensar em Grande, Faz Agora', 'Tocha e José Serra')

print(f'O livro "{book1.titulo}" foi realizado por "{book1.autor}" ')
print(f'O livro "{book2.titulo}" foi realizado por "{book2.autor}" ')
print(f'O livro "{book3.titulo}" foi realizado por "{book3.autor}" ')