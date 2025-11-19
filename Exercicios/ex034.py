# Faça um programa que leia 10 números e
# conte quantos deles são pares.

pares = 0

for e in range(1, 11):
    num = int(input('Digite um numero : '))
    if num % 2 == 0:
        print(f"O número {num} é par.")
        pares = pares + 1
    else:
        print(f"O número {num} é ímpar.")

print('Fim da verificação dos numeros !')
print(f'- Total de pares : {pares}')
