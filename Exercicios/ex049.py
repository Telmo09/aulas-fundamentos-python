# Desenvolva o jogo par ou ímpar.
# O jogo só será interrompido quando o jogador perder
# e deverá exibir o total de vitórias consecutivas.

from random import randint

print('--- PAR OU IMPAR ---')
print('o CPU vai indicar um numero aleatorio')
print('se a SOMA for PAR , ganhas')
print('se a SOMA for IMPAR, perdeu')
tentativas = 0

while True:
    CPU = randint(0, 1)
    print()
    User = int(input('Introduza um número : '))
    soma = CPU + User
    if soma % 2 == 0:
        print('Par')
        tentativas += 1
        print(f'Já vais em {tentativas}x streak !')
    else:
        print('Calhou Impar ! Perdeu.')
        break

print(f'Conseguiu {tentativas}x streak !')