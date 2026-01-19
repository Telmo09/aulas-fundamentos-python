'''
Crie uma classe chamada “Círculo” que possua um atributo privado para armazenar:
- o raio
- métodos getters
- método setters
para definir o raio, calcular a área e o perímetro do círculo.
'''

from math import pi

def menu(circulo):
    while True:
        print(f'\n--- Raio : {circulo.raio} --- ')
        print('[ 1 ] - Definir o raio')
        print('[ 2 ] - Calcular a area do circulo')
        print('[ 3 ] - Calcular perimetro do circulo')
        print('[ 4 ] - Sair')
        opcao = int(input('Selecione uma opção: '))
        if opcao == 1:
            novo_raio = int(input('Defina um novo raio : '))
            circulo.raio = novo_raio
        elif opcao == 2:
            circulo.area()
        elif opcao == 3:
            circulo.perimetro()
        elif opcao == 4:
            break
        else:
            print('Opção Invalida, tente novamente.')

class Circulo:
    def __init__(self):
        self.__raio = 5

    @property
    def raio(self):
        return self.__raio

    @raio.setter
    def raio(self, novo_raio):
        self.__raio = novo_raio

    def area(self):
        area = pi * (self.__raio * self.__raio)
        print(f'A area do circulo é {area:.2f}')

    def perimetro(self):
        perimetro = 2 * pi * self.__raio
        print(f'O perimetro do circulo é de {perimetro:.2f}')



circulo = Circulo()
menu(circulo)
