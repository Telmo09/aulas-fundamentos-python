'''
Crie um programa que tenha uma função que converta a temperatura:
- de Celsius para Fahrenheit.
'''
from time import sleep

def valores():
    temperatura = int(input('\nDigite uma temperatura: '))

    while True:
        type = input('[C/F] Inseriu em Celcius ou Fahrenheit ? ').upper()
        if type == 'C' or type == 'F':
            break
        else:
            print('Coloque um valor valido')

    if type == 'C':
        ConvertC(temperatura)
    if type == 'F':
        ConvertF(temperatura)

def ConvertC(temperatura):
    sleep(0.3)
    print(f'\nA temperatura inserida foi {temperatura}ºC')
    converter = (temperatura * 1.8) + 32
    sleep(0.3)
    print(f'A temperatura em Fahrenheit é de {converter}ºF \n')
    repetir()

def ConvertF(temperatura):
    sleep(0.3)
    print(f'\nA temperatura inserida foi {temperatura}ºF')
    converter = (temperatura - 32) / 1.8
    sleep(0.3)
    print(f'A temperatura em Fahrenheit é de {converter}ºC \n')
    repetir()

def repetir():
    while True:
        continuar = input('[S/N] Deseja continuar ? ').upper()
        if continuar == 'S' or continuar == 'N':
            break
        else:
            print('Introduza um valor valido !')

    if continuar == 'S':
        valores()
    else:
        print('Fim do programa !')


def menu():
    print('Conversor de temperaturas')
    print('Disponivel o seguinte :')
    print('- De Celcius para Fahrenheit')
    print('- De Fahrenheit para Celcius')
    sleep(1.5)
    valores()

menu()