'''
Melhore o exercício 67 para que permita a entrada de vários jogadores.
Defina um sistema de visualização que permita ao utilizar
procurar pelos resultados de um jogador específico.
'''

import os

jogador = dict()
cont = 'S'

while cont == 'S':
    jogador['Nome'] = input('Qual o Nome do jogador ? ')
    jogador['Partidas'] = int(input('Quantos jogos realizou ? '))
    jogador['Golos'] = int(input('Quantos golos marcou ? '))
    jogador['Media'] = jogador['Golos'] / jogador['Partidas']

    cont = input('[S/N] Deseja continuar ? ')

    for chave, valor in jogador.items():
        print(f'{chave} -> {valor}')

opcao = 0
while opcao != 6:
    print('--- SISTEMA DE CONSULTA DE JOGADORES ---')
    print('[ 1 ] - Lista de jogadores')
    print('[ 2 ] - Melhor Marcador')
    print('[ 3 ] - Pesquisar pelo nome')
    print('[ 4 ] - Ranking')
    print('[ 5 ] - Registar novo jogador')
    print('[ 6 ] - Sair')
    opcao = int(input('Introduza uma opção : '))

    if opcao == 1:
        print('--- LISTA DE JOGADORES ---')
        contador = 1
        for jogador in jogadores:
            print(f'{contador} - {jogador['Nome']}')
            contador += 1
        os.system('Pause')

    elif opcao == 2:
        print('--- MELHOR MARCADOR ---')
        nome = ''
        golos = 0

        for jogador in jogadores:
            if jogador['Golos']:
                golos = jogador['Golos']
                nome = jogador['Nome']

        print(f'{nome} -> {golos} golos marcados.')
        os.system('Pause')