# Desenvolva um programa que leia um número qualquer e que mostre o seu fatorial.

print('--- Fatorial dos numeros ---')
num = int(input('Introduza um número : '))
contagem = num
conta = num

while True:
    if contagem != 1:
        conta = conta * (contagem - 1)
        contagem -= 1
    else:
        break

print(f'Fatorial de {num} é de {conta}')

