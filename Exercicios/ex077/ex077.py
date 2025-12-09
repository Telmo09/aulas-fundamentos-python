'''
Crie um programa que tenha uma função que vai receber como parâmetro o ano de nascimento de uma pessoa
e que crie um ficheiro que informe
- se a pessoa já pode tirar a carta de condução,
- se precisa de autorização do encarregado de educação
- ou se não pode.

+18 anos – pode
-16 anos – não pode
-18 e +16 – com autorização
'''
from pathlib import Path
from datetime import datetime

def calculo(nascimento, nome):
    ano_atual = datetime.now().year
    idade = ano_atual - nascimento
    print(f'\n{nome} tem {idade} anos\n')
    resultado(idade, nome)

def resultado(idade, nome):
    caminho = Path(r'resultados.txt')

    if idade >  18:
        with caminho.open('a', encoding='UTF-8', errors='ignore') as file:
            file.write(f'{nome}, {idade}.\nPode tirar a carta de condução\n\n')
            print('Pode tirar a carta de condução')
    elif idade < 16:
        with caminho.open('a', encoding='UTF-8', errors='ignore') as file:
            file.write(f'{nome}, {idade}.\nNão pode tirar a carta de condução\n\n')
            print('Não pode tirar a carta de condução')
    else:
        with caminho.open('a', encoding='UTF-8', errors='ignore') as file:
            file.write(f'{nome}, {idade}.\nPode tirar a carta de condução, com autorização.\n\n')
            print('Pode tirar a carta de condução, com autorização.')

def inicio():
    print('--- Carta de condução ---')
    nome = input('Indique o seu nome: ')
    nascimento = int(input('Indique a sua data de nascimento: '))
    calculo(nascimento,nome)

inicio()
