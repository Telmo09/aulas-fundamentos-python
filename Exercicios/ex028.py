# Crie o jogo da adivinha v1.0.
# O computador deve “pensar” num número de 0 a 7 e
# o utilizador deve adivinhar o número escolhido.
# O programa deve apresentar se o utilizador venceu ou perdeu.

from random import randint

print(' --- JOGO DA ADIVINHA 1.0 ---')

print('Escolhi um numero entre 0 e 7')
print('És capaz de adivinhar ?')
jogada =  int(input('---> '))
aleatorio = randint(0 , 7)

if jogada == aleatorio:
    print('Acertou !')
else:
    print('Perdeu !')
    print(f'Eu pensei no {aleatorio}')