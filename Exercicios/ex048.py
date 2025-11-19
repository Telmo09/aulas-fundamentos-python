# Tabuada V2.0
# Faça um programa que mostre a tabuada de vários números inseridos pelo utilizador.
# O programa deverá ser interrompido quando o número inserido for negativo ou 0.

print('--- TABUADA ---')

num = 1
calc = 1

while calc != 10:
    while num > 0:
        num = int(input('Digite um numero : '))
        if num <1:
            print('Numero invalido, tente novamente !')
            num = 1
        else:
            while calc != 11:
                print(f'{num} x {calc} = {num * calc}')
                calc += 1
                if calc == 11:
                    calc = 1
                    break