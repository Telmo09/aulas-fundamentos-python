# Faça um programa que leia o ano de
# nascimento de 7 pessoas e mostre
# quantas são maiores de idade e quantas
# não são maiores de idade.

from datetime import  datetime

ano_atual = datetime.now().year
menor = 0
adulto = 0

for f in range(0, 7):
    ano_nascimento = int(input(f'Digite o ano de nascimento da {f+1} pessoa : '))
    idade = ano_atual - ano_nascimento

    if idade < 18:
        menor = menor +1
    else:
        adulto = adulto +1

print('Fim da verificação das idades !')
print(f' - Numero de menores : {menor}')
print(f' - Numero de adultos : {adulto}')
