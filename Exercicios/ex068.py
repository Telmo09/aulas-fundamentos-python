'''
Crie um programa que leia :
- o nome
- sexo
- idade de várias pessoas
guardando cada dado num dicionário e todos os dicionários numa lista.

No final mostre:
a) Quantas pessoas foram registadas;
b) Qual a média de idades do grupo;
c) Quantas mulheres foram registadas;
d) Quantos homens com idade acima da média foram registados.
'''

lista = list()
ordem = 0
cont = 'S'

# Registo dos dados :
UserRegisted = 0
idade = 0
idade_total = 0
mulheres = 0

while cont == 'S':
    grupo = dict()
    ordem += 1

    # Nome
    grupo['Nome'] = input(f'\nDigite o nome da {ordem}ª pessoa: ')

    # Sexo
    sexo = input(f'[F/M] Digite o sexo de {grupo["Nome"]}: ')
    if sexo == 'F':
        mulheres += 1
    grupo['Sexo'] = sexo

    # Idade
    idade = int(input(f'Digite a idade de {grupo["Nome"]}: '))
    idade_total += idade
    grupo['Idade'] = idade

    cont = input('\n[S/N] Deseja Continuar ? ')

    UserRegisted += 1

# Registo dos dados [P2] :
media_idade = idade_total / UserRegisted
homens = 1

# Contar homens acima da média
homens_acima_media = 0
for pessoa in lista:
    if pessoa['Sexo'] == 'M' and pessoa['Idade'] > media_idade:
        homens_acima_media += 1

print()
print('--- Dados Registados ---')
print(f'Pessoas Registadas : {UserRegisted}')
print(f'A media das idades é de {media_idade}')
print(f'Foram registados {mulheres} mulheres')
print(f'Homens com idade acima da media : {homens_acima_media}')




