# Faça um programa que simule uma contagem regressiva para a passagem de
# ano, de 10 até 0, com 1 segundo de pausa entre eles.

from time import sleep

for contagem in range(10,0,-1):
    print(f'{contagem}')
    sleep(1)