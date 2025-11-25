def cabecalho(txt):
    print('-' * 20)
    print(f'{txt:-^20}')
    print('-' * 20)


def soma(num1, num2):
    cabecalho('SOMA')
    print(f'{num1} + {num2} = {num1 + num2}')

def subtracao(num1, num2):
    cabecalho('SUBTRACAO')
    print(f'{num1} - {num2} = {num1 - num2}')

def multiplicacao(num1, num2):
    cabecalho('MULTIPLICAÇÃO')
    print(f'{num1} x {num2} = {num1 * num2}')

def divisao(num1, num2):
    cabecalho('DIVISAO')
    print(f'{num1} / {num2} = {num1 / num2}')

def menu():
    n1 = int(input('Digite um numero: '))
    n2 = int(input('Digite outro numero: '))

    while True:
        cabecalho('MENU')
        print('[ 1 ] - Soma')
        print('[ 2 ] - Subtração')
        print('[ 3 ] - Multiplicação')
        print('[ 4 ] - Divisão')
        print('[ 5 ] - Sair')
        opcao = int(input('Selecione uma opçao : '))

        if opcao == 1:
            soma(n1, n2)
        elif opcao == 2:
            subtracao(n1, n2)
        elif opcao == 3:
            multiplicacao(n1, n2)
        elif opcao == 4:
            divisao(n1, n2)
        elif opcao == 5:
            break
        else:
            print('Opção Invalida')

# ##################
# PROGRAMA PRINCIPAL
# ##################
menu()
