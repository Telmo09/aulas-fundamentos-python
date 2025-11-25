'''
Crie um programa que tenha uma função camada area()
que recebe as dimensoes de um terreno e mostre a area do terreno
'''

def cabecalho(txt):
    print('-' * 30)
    print(f'{ txt :-^30}')
    print('-' * 30)

def area(num1, num2):
    cabecalho('Area do Terreno')
    print(f'A área do terreno é de {num1 * num2}')

def menu():
    comprimento = int(input('Digite o comprimento do terreno : '))
    largura = int(input('Digite a largura do terreno : '))
    area(comprimento, largura)

menu()