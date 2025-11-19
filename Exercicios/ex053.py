# Crie um programa que gere 5 números aleatórios dentro de um tuple.
# Depois mostra a listagem de números gerados, o menor e o maior.

from random import randint

numgerados = (randint(0,100),
              randint(0,100),
              randint(0,100),
              randint(0,100),
              randint(0,100))

print('Numeros gerados :')
menor = maior = 0

for numero in numgerados:
    print(f'\t{numero}', end=' ')

    if numero == numgerados[0]:
        menor = numero
        maior = numgerados

    else:
        if numero > maior:
            maior = numero

        if numero < menor:
            menor = numero

print()
print(f'O maior valor encontrado é {maior}')
print(f'O menor valor encontrado é {menor}')