# Crie um programa que leia vários números inteiros e que termine apenas
# quando o utilizador digitar a opção para parar.
# No final mostre quantos números o utilizador inseriu e qual a soma entre eles.

num = ''
soma = 0
contagem = 0

while num !=0:
    num = int(input('Insere um número : '))
    soma += num
    contagem += 1

print(f'Foram usados {contagem-1} numeros.')
print(f'A soma deles é de {soma}')