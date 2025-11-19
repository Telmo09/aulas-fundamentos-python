# Faça um programa que leia 5 números
# inteiros e mostre a soma desses números.

numero = 0

for countdown in range(0,5):
    contar = int(input('Digite um numero : '))
    numero = numero + contar
    print(f'Soma Atual : {numero} ({countdown+1}/5)')
