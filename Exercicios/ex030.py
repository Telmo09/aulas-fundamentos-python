# Crie o jogo pedra, papel, tesoura.

import random
escolha_bot = random.randint(1,3)

if escolha_bot == 1:
    print('Escolhi pedra')
elif escolha_bot == 2:
    print('Escolhi papel')
elif escolha_bot == 3:
    print('Escolhi tesoura')

print('Pedra Papel Tesoura')
print('[1] - Pedra')
print('[2] - Papel')
print('[3] - Tesoura')
jogada = int(input('Qual será a sua jogada ? '))

if escolha_bot == 1 and jogada == 1:
    print('Empate ! Ambos escolhemos pedra')
elif escolha_bot == 1 and jogada == 2:
    print('Ganhaste ! Papel ganha a Pedra')
elif escolha_bot == 1 and jogada == 3:
    print('Perdeste ! Tesoura perde a Pedra')
elif escolha_bot == 2 and jogada == 1:
    print('Perdeste ! Pedra perde a Papel')
elif escolha_bot == 2 and jogada == 2:
    print('Empate ! Ambos escolhemos Papel')
elif escolha_bot == 2 and jogada == 3:
    print('Ganhaste ! Tesoura ganha a Papel')
elif escolha_bot == 3 and jogada == 1:
    print('Ganhaste ! Pedra ganha a Tesoura')
elif escolha_bot == 3 and jogada == 2:
    print('Pereste ! Papel perde a Tesoura')
elif escolha_bot == 3 and jogada == 3:
    print('Emprate ! Ambos escolhemos Tesoura')