'''
Crie um programa que guarde o aproveitamento de um jogador de futebol.
O programa deverá ler :
- o nome,
- quantos jogos jogou
- e a quantidade de golos
guardar tudo num dicionário.

No dicionário, deve calcular a média de golos por jogo.
'''

jogador = dict()

jogador['Nome'] = input('Qual o Nome do jogador ? ')
jogador['Partidas'] = int(input('Quantos jogos realizou ? '))
jogador['Golos'] = int(input('Quantos golos marcou ? '))
jogador['Media'] = jogador['Golos'] / jogador['Partidas']

print(jogador)

for chave, valor in jogador.items():
    print(f'{chave} -> {valor}')