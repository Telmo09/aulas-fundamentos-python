# Crie um programa que leia 4 valores e guarde-os num tuple.
# No final exiba:
#
# a) Quantas vezes aparecer o número 7.
# b) Em que posição foi digitado o número 5.
# c) Quais são os números pares.
#
# O programa deve informar quando não encontrar resposta.

from time import sleep

user = (int(input('[1/4] Adicione um numero : ')),
        int(input('[2/4] Adicione um numero : ')),
        int(input('[3/4] Adicione um numero : ')),
        int(input('[4/4] Adicione um numero : ')))

sleep(0.5)
print()
print('Segundo os dados introduzidos, informo o seguinte :')
sleep(1)
print(f'Numeros introduzidos : {user}')
print()

contagem7 = 0
for a in user:
    if a == 7:
        contagem7 += 1
sleep(1)
print(f'Aparece {contagem7} vezes o numero 7')

for indice, numero in enumerate(user):
    if numero == 5:
        sleep(1)
        print(f'[POS {indice+1}] O numero "5" aparece ')

for indice, numero in enumerate(user):
    if numero % 2 == 0:
        sleep(1)
        print(f'[POS {indice+1}] O numero {numero} é par')

sleep(1)
print()
print('Fim do programa')