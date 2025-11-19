# Crie um programa que leia dois números inteiros e compare-os da seguinte forma:
#
# - O primeiro número é maior;
# - O segundo número é maior;
# - Os números são iguais.

numero1 = int(input('Insere um numero : '))
numero2 = int(input('Insere outro numero : '))

if numero1 > numero2:
    print('O primeiro número é maior')
elif numero1 < numero2:
    print('O segundo número é maior')
else:
    print('Os números são igual')