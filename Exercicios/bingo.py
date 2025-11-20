from random import randint
from time import sleep

jogador1 = [15, 19, 13, 41, 95]
jogador2 = [23, 42, 71, 4, 10]

P1 = 0
P2 = 0
sorteio = []

for rodada in range(1, 100):
    sleep(0.2)
    while True:
        num = randint(1, 100)
        if num not in sorteio:
            sorteio.append(num)
            break

    print(f"Número sorteado ({rodada}): {num}")

    if num in jogador1:
        P1 += 1
        print("Jogador 1 acertou!")
        print(f"Resultado | jogador 1: {P1} pontos // jogador 2: {P2} pontos ")
    if num in jogador2:
        P2 += 1
        print("Jogador 2 acertou!")
        print(f"Resultado | jogador 1: {P1} pontos // jogador 2: {P2} pontos ")

    # Verifica vencedor
    if P1 == 5:
        print("Terminou! Jogador 1 ganhou!")
        break
    if P2 == 5:
        print("Terminou! Jogador 2 ganhou!")
        break