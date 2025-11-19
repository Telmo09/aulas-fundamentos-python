# Crie um programa que tenha um tuple com nomes de jogos
# e os seus respetivos preços em sequência.
#
# No final, mostre uma listagem de preços organizados como tabela.

from time import sleep

jogos = ('EA SPORTS FC 26', 'Remnant II', 'Left 4 Dead 2', 'Dying Light', 'Ghost of Tsushima',
         'Euro Truck Simulator 2', 'Stray', 'Grand Theft Auto V', 'Red Dead Redemption 2',
         'Cyberpunk 2077', 'Borderlands 4', 'Backrooms: Escape Together', 'PEAK', 'R.E.P.O.')
preco = ('69,99€', '49,99€', '9,75€', '59,99€', '59,99€',
         '19,99€', '27,99€', '29,99€', '59,99€', '59,99€',
         '69,99€', '9,75€', '7,49€', '9,75€')

print()
print(f'{" Lista de Jogos ":^50}')
print(f'{"Jogo": <46} Preço')
for c in range(len(jogos)):
    jogo = jogos[c]
    valor = preco[c]

    lenjogo = len(jogo)
    lenpreco = len(valor)
    lentotal = lenjogo + lenpreco
    espaco = '-' * (50 - lentotal)

    print(f'{jogos[c]} {espaco} {preco[c]}')
    sleep(0.3)