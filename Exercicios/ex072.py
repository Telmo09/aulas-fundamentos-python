'''
Crie um programa que tenha uma função que receba 3 parâmetros:
inicio, fim e passo.
O programa deve realizar 3 contagens através da função.

a) De 1 até 20, de 2 em 2
b) De 10 até 0, de 1 em 1
c) Contagem personalizada
'''
from time import sleep

def contagem1():
    for c in range(0,20,2):
        print(c+2)
        sleep(0.2)
    print('Contagem Terminada !')
    sleep(0.5)
    menu()

def contagem2():
    for c in range(10,-1,-1):
        print(c)
        sleep(0.2)
    print('Contagem Terminada !')
    sleep(0.5)
    menu()

def contagem3(inicio, fim, passo):
    for c in range(inicio, fim, passo):
        print(c)
        sleep(0.2)
    print('Contagem Terminada !')
    sleep(0.5)
    menu()


def menu():
    while True:
        print('')
        print('--- Contagem de numeros ---')
        print('[ 1 ] - De 1 até 20, de 2 em 2')
        print('[ 2 ] - De 10 até 0, de 1 em 1')
        print('[ 3 ] - Contagem personalizada')
        print('[ 4 ] - Sair')
        opcao = int(input('Indique uma opção: '))

        if opcao == 1:
            contagem1()
        if opcao == 2:
            contagem2()
        elif opcao == 3:
            inicio = int(input('Indique o numero que deseja iniciar: '))
            fim = int(input('Indique o numero que deseja terminar: '))
            passo = int(input('Indique o intervalo em cada numero: '))

            if inicio > fim :
                passo = -passo
                fim = fim - 1
            else :
                fim = fim + 1

            contagem3(inicio, fim, passo)
        elif opcao == 4:
            print('Saindo ...')
            break
        else:
            print('Opçao Invalida !')
menu()