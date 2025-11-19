# Crie um programa com um tuple
# com os 20 primeiros classificados do Campeonato Espanhol de Futebol. Depois mostre:
#
# a) Os primeiros 5 classificados.
# b) Os últimos 4 classificados.
# c) Uma lista com as equipas por ordem alfabética.
# d) A posição da equipa Las Palmas.

from time import sleep

campeonato = ('Real Madrid' , 'Barcelona', 'Vilarreal CF', 'Betis', 'Atletic Madrir',
                  'Sevilha FC', 'Elche CF', 'Atletico Bilbao', 'RCD de Barcelona', 'Desportivo Alavés',
                  'Getafe CF', 'CF Osanuna', 'Levante UD', 'Rayo', 'Valencia CF',
                  'RC Celta de Vigo', 'Real Oviedo CF', 'Girona FC', 'Real Sociedad', 'Rcd Mallorca FC')

pontos = (21, 19, 16, 15, 13,
          13, 13, 13, 12, 11,
          11, 10, 8, 8, 8,
          6, 6, 6, 5, 5)

while True:

    print()
    print('- - - Campeonato Espanhol de Futebol - - -')
    print('[1] - Os primeiros 5 classificados.')
    print('[2] - Os últimos 4 classificados.')
    print('[3] - Uma lista com as equipas por ordem alfabética.')
    print('[4] - A posição da equipa Las Palmas.')
    print('[5] - Terminar o programa')
    opcao = int(input('O que deseja ver ? '))
    print()

    if opcao == 1:
        print('Os primeiros 5 classificados são :')
        for c in range(0, 20):
            if c < 5:
                print(f'[{c+1}º lugar] {campeonato[c]}, com {pontos[c]} pontos')
                sleep(0.5)

    elif opcao == 2:
        print('Os ultimos 4 classificados são :')
        for c in range(0, 20):
            if c > 15:
                print(f'[{c + 1}º lugar] {campeonato[c]}, com {pontos[c]} pontos')
                sleep(0.5)

    elif opcao == 3:
        for campeonato in sorted(campeonato):
            print('\t', campeonato)
            sleep(0.5)

    elif opcao == 4:
        sleep(0.5)
        na_lista = False
        indice_las_palmas = ''
        for indice, equipa in enumerate(campeonato):
            if equipa == 'Las Palmas':
                na_lista = True
                indice_las_palmas = indice
        if na_lista:
            print(f'[{indice_las_palmas + 1}º lugar] '
                  f'{campeonato[indice_las_palmas]}, com {pontos[indice_las_palmas]} pontos')
        else:
            print('A equipa "Las Palmas": não se encontra no top 20')
        sleep(0.5)

    elif opcao == 5:
        break

    else:
        print('⚠️ Opção inválida, por favor selecione uma opção válida.')