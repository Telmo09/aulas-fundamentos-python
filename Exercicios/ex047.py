# Crie um programa que leia várias notas introduzidas pelo utilizador.
# No final mostre:
# - quantas notas o utilizador inseriu
# - qual a média entre elas
# - qual a maior nota
# - qual a menor nota

num = ''
contagem = soma = maior_num = menor_num = 0

while num !=0:
    if contagem == 0:
        num = int(input(f'Digite a {contagem+1}ª nota : '))
        maior_num = num
        menor_num = num
        soma += num
        contagem += 1
    else:
        num = int(input(f'Digite a {contagem+1}ª nota : '))
        soma += num
        contagem += 1
        if num > maior_num and num != 0:
            maior_num = num
        if num < menor_num and num != 0:
            menor_num = num

print(f'Foram usados {contagem-1} numeros.')
media = soma / (contagem-1)
print(f'A média das notas é de {media:.2f}')
print(f'Maior numero é {maior_num}')
print(f'Menor numero é {menor_num}')