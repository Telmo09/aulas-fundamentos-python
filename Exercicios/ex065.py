from random import randint

'''
qtd_jogador = int(input('Quantos Jogadores vao jogar ? '))
dado = list()
jogador = dict()

for c in range(qtd_jogador):
    while True:
        num = randint(1,6) # gerar dado de 1 a 6
        if num in dado: # evitar duplicados
            continue
        else:
            dado.append(num)
            break

Players = []
for c in range(qtd_jogador):
    jogador['Nome'] = input(f'Indique o nome do jogador {c+1}: ')
    jogador['Ordem'] = dado[c]

    Players.append(jogador.copy())

print(Players)
'''

    # Correção
qtd_jogador = int(input('Quantos Jogadores vao jogar ? '))
jogadores = {}

for c in range(qtd_jogador):
    nome = input(f'Digite o nome do {c+1}º jogador: ')
    jogada = randint(1,6) # dado lançado
    jogadores[nome] = jogada

    # jogadores[input(f'Digite o nome do {c+1}º jogador: ')] = randint(1,6)

auxiliar = jogadores.copy()
ranking = list()

while auxiliar:
    maior_jogador = ''
    maior_valor = 0

    for jogador, jogada in auxiliar.items():
        if jogada > maior_valor:
            maior_jogador = jogador
            maior_valor = jogada

    ranking.append((maior_jogador, maior_valor))
    del auxiliar[maior_jogador]

print(ranking)

for tupla in ranking:
    for elemento in tupla:
        print(f'{elemento}')





