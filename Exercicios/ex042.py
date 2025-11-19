# Crie o jogo da adivinha v2.0. O computador deve “pensar” num número
# de 0 a 10 e o utilizador deve adivinhar o número escolhido.
# Só que agora o jogador vai tentar adivinhar até acertar.
# No final mostre quantas tentativas foram necessárias.

from random import randint

print('--- Jogo da Adivinha v2.0 ---')
print('Pensei num numero de 0 a 10')
print()
CPU = randint(0,10)
User = ''
alto = 11
baixo = -1
tentativas = 0

while True:
    user = int(input('Introduza um numero : '))
    tentativas += 1
    if user == CPU:
        print('Acertou !')
        break
    elif CPU > user:
        print('⬆️ Errou, tente mais alto')
        baixo = user
        print(f'Dica : é entre {baixo+1} e {alto-1}')
        print()
    elif CPU < user:
        print('⬇️ Errou, tente mais baixo')
        alto = user
        print(f'Dica : é entre {baixo+1} e {alto-1}')
        print()

print('--- --- ---')
print(f'Demorou {tentativas} tentativas !')
print('Muitos Parabens !')