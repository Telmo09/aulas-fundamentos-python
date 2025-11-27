'''
Crie um programa que tenha uma função que receba o nome de um aluno e uma lista das suas notas.
Ele deve calcular a média do aluno e mostrar no ecrã:
- o nome do aluno
- a sua média
- e se ele ficou aprovado ou não.
'''

from time import sleep

def reportcard():
    notas = 0
    disciplinas = list()
    lista_notas = list()

    nome = input('Indique o seu Nome: ')

    for c in range(0,5):
        disciplina = input(f'Digite a {c+1}º disciplina: ')
        disciplinas.append(disciplina)
    print()

    for d in range(0,5):
        nota = int(input(f'Digite a nota de {disciplinas[d]}: '))
        lista_notas.append(nota)
        notas += nota
    print()

    media = notas / 5
    final(disciplinas, lista_notas, nome, media)

def final(disciplinas, lista_notas, nome, media):
    sleep(0.2)
    print('--- Report Card ---')
    sleep(0.2)
    print(f'Nome : {nome}')
    sleep(0.2)
    for e in range(0,5):
        print(f'{disciplinas[e]} tirou {lista_notas[e]}')
        sleep(0.5)
    print(f'A sua media foi de {media}')
    sleep(0.2)
    if media < 9.5:
        print('Reprovou !')
    else:
        print('Passou !')


def menu():
    print('--- Report Card ---')
    print('Insere os seus dados\n')
    reportcard()

menu()