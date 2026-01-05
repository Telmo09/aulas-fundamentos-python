'''
Crie um programa com uma função que vai funcionar como a função input(),
no entanto vai fazer a validação para aceitar apenas um valor numérico.
'''

def start():
    print('--- ANALISE DE VALOR ---')

    while True:
        try:
            value = int(input('Introduza um valor: '))
            break
        except ValueError:
            print('⚠️ Por favor insere um numero')

    print(f'Valor inserido: {value}')

start()




