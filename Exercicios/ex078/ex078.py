'''
Crie um programa com uma função chamada fatorial(), que receba dois parâmetros:
- o primeiro será o número a calcular o fatorial
- e o segundo será opcional e lógico que indique se será exibido ou não o processo de cálculo do fatorial.
O fatorial deve ser guardado num ficheiro txt.
'''
from time import sleep

def fatorial(base, option):
    from pathlib import Path
    caminho = Path(r'fatorial.txt')

    num2 = base -1

    calc = base * num2
    print(f'{base} x {num2} = {calc}')
    with caminho.open('a', encoding='UTF-8', errors='ignore') as file:
        file.write(f'{base} x {num2} = {calc}' + '\n')

    while num2 != 1:
        sleep(0.3)
        num2 -= 1
        conta = calc * num2
        if option == 'S':
            print(f'{calc} * {num2} = {conta}')

        with caminho.open('a', encoding='UTF-8', errors='ignore') as file:
            file.write(f'{calc} x {num2} = {conta}' + '\n')

        calc = conta

    with caminho.open('a', encoding='UTF-8', errors='ignore') as file:
        file.write('\n')

def menu():
    print('--- Calculo de Fatorial ---')
    base = int(input('Indique o numero a fazer o fatorial: '))
    option = 'A'
    while option != 'S' and option != 'N':
        option = input('[S/N] Deseja exibir no ecrã ? ').upper()
        if option != 'S' and option != 'N':
            print('⚠️ Opção invalida, indique com S ou N')
    fatorial(base, option)

menu()