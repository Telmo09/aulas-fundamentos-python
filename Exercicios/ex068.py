'''
Crie um programa que leia:
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
cont = 'S'

# Registo dos dados:
qtd_pessoas = 0
idade = 0
idade_total = 0
mulheres = 0

grupo = dict()
while cont == 'S':
    qtd_pessoas += 1

    # Nome
    grupo['Nome'] = input(f'\nDigite o nome da {qtd_pessoas}ª pessoa: ')

    # Sexo
    while True:
        grupo['sexo'] = input(f'[F/M] Digite o sexo de {grupo["Nome"]}: ').strip().upper()

        if grupo['sexo'] != 'M' and grupo['sexo'] != 'F':
            print('Por favor introduza um sexo valido')
            continue
        else:
            if grupo['sexo'] == 'F':
                mulheres += 1
            break

    # Idade
    grupo['idade'] = int(input(f'Digite a idade de {grupo["Nome"]}: '))
    idade_total += grupo['idade']

    # Novo registo ? S/N
    cont = input('\n[S/N] Criar novo registo ? ')

# Registo dos dados [P2] :
media_idade = idade_total / qtd_pessoas

# Homens acima da média
qtd_homens_acima_media = 0
for c in grupo:
    if grupo['sexo'] == 'M':
        if grupo['idade'] > media_idade:
            qtd_homens_acima_media += 1

# Finalização dos dados:
print()
print('##############################')
print('--- Dados Registados ---')
print(f'Pessoas Registadas : {qtd_pessoas}')
print(f'A media das idades é de {media_idade}')
print(f'Foram registados {mulheres} mulheres')
print(f'Homens com idade acima da media : {qtd_homens_acima_media}')