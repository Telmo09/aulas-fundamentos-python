'''
Crie um programa que tenha uma função que receba um número inteiro
e mostre a tabuada desse número.
'''

from time import sleep

def calcular(tabuada, multiplic):
    for c in range(0,multiplic):
        print(f'{tabuada} x {c+1} = {tabuada * (c+1)}')
        sleep(0.3)

def menu():
    print('--- TABUADA ---')
    tabuada = int(input('Introduza um numero: '))
    multiplic = int(input('Quer tabuada até quanto ? '))
    calcular(tabuada, multiplic)


menu()