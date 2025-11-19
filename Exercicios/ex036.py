# Faça um programa que mostre a tabuada
# de um número introduzido pelo utilizador.

print('--- TABUADA ---')
num = int(input('Introduza um numero : '))

for f in range(0,10):
    print(f'{num} x {f+1} = {num * (f +1)}')