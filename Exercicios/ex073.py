'''
Crie um programa que tenha uma função que receba vários parâmetros como valores inteiros.
O programa deve analisar todos os valores e dizer qual deles é o maior.
'''

def receber():
    num_listagem = list()
    maior_numero = 0
    cont = 0

    while True:
        cont += 1
        num = int(input(f'Digite o {cont}º numero: '))

        if num == 0:
            break

        if num > maior_numero:
            maior_numero = num

        num_listagem.append(num)

    resultados(num_listagem, maior_numero)

def resultados(num_listagem, maior_numero):
    print('Valores introduzidos foram os seguintes :')
    print(f'{num_listagem}')
    print(f'O maior numero é {maior_numero}')

def menu():
    print('--- Analise de numeros ---')
    print('Introduza diversos valores')
    print('Inserir 0 dá como terminado')
    receber()

menu()