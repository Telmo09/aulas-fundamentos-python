# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa registada o programa deverá perguntar se o utilizador quer continuar ou não.
# No final mostre:
# a) Quantas pessoas têm mais de 25 anos.
# b) Quantos homens com menos 17 anos foram registados.
# c) Quantas mulheres foram registadas.
# d) Quantos menores de idade foram registados.

genero = ''
idade = ''
reg = ''
adulto_25 = 0
menores_homem = 0
mulheres = 0
menores = 0
contagem = 1

while reg != 'S':
    reg = ''
    idade = int(input(f'Introduza a idade da {contagem}ª pessoa : '))
    if idade <= 0:
        print('Idade invalida !')
        continue
    if idade >= 25:
        adulto_25 += 1
    else:
        menores += 1
    while genero != 'M' and genero != 'F':
        genero = input(f'Introduza o genero da {contagem}ª pessoa : ').upper().strip()
        if idade < 18 and genero == 'M':
            menores_homem += 1
        if genero == 'F':
            mulheres += 1
    while reg != 'N' and reg != 'S':
        contagem += 1
        genero = ''
        reg = input('[S/N] Deseja parar o registo ? ').upper().strip()

print('- - - Total dos resultados - - -')
print(f'Numero de adultos (com mais de 25) = {adulto_25}')
print(f'Numero de menores masculinos = {menores_homem}')
print(f'Numero de mulheres = {mulheres}')
print(f'Numero de menores = {menores}')