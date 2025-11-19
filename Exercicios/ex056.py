# Crie um programa que leia 5 números e guarde-os numa lista.
# No final mostre o maior e o menor valor e a respetiva posição na lista.

numeros = list()

for c in range(0,5):
    addnum = int(input('Digite um numero : '))
    numeros.append(addnum)

MaiorNum = 0
MenorNum = 0
MaiorIndice = 0
MenorIndice = 0

print()
for indice, numero in enumerate(numeros):
    if indice == 0:
        MaiorNum = numero
        MaiorIndice = indice
        MenorNum = numero
        MenorIndice = indice
        continue

    if numero > MaiorNum:
        MaiorNum = numero
        MaiorIndice = indice
    if numero < MenorNum:
        MenorNum = numero
        MenorIndice = indice

print(f'O maior numero é {MaiorNum}, situado na {MaiorIndice+1}º posição')
print(f'O menor numero é {MenorNum}, situada na {MenorIndice+1}º posição')
