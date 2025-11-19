# Faça um programa que leia a idade de
# 10 pessoas. No final mostre qual foi a
# maior idade lida e a menor.

idade = int(input('Digite uma idade : '))
print(' ')

menor = idade
maior = idade

for f in range (1, 10):
    idade = int(input('Digite uma idade : '))

    if idade < menor:
        menor = idade
        print(' ')
    elif idade > maior:
        maior = idade
        print(' ')
    else:
        print(' ')

print(f'Maior idade : {maior}')
print(f'Menor idade : {menor}')

