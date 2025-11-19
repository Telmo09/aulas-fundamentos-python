# Faça um programa que leia um número inteiro
# e diga se ele é ou não um número primo.

numero = int(input("Digite um número: "))

if numero < 2:
    print(f"{numero} não é um número primo.")
else:
    n_primo = True

    for num in range(2, numero):
        if numero % num == 0:
            n_primo = False
            break

    if n_primo:
        print(f"{numero} é um número primo!")
    else:
        print(f"{numero} não é um número primo.")
