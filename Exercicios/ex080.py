'''
Crie um programa com uma função que vai receber várias notas de alunos
e vai retornar um dicionário com o seguinte:

a) Quantidade de notas
b) A maior nota
c) A média da turma
d) A situação (lógico opcional)
    >12 – boa
    <9,5 – fraca
    >9,5 e <12 - razoável
'''

def adicionar(turma):
    continua = 'S'

    while continua == 'S':
        aluno = {}
        contagem = len(turma) + 1

        aluno["Nome"] = input(f'Indique o nome do/a {contagem} aluno/a: ')
        aluno["Nota"] = float(input(f'Indique a nota do/a {aluno["Nome"]}: '))

        turma.append(aluno)

        continua = input('[S/N] Deseja adicionar mais? ').upper()

        while continua != 'S' and continua != 'N':
            continua = input('[S/N] Deseja adicionar mais? ').upper()

        resultados(turma)


def resultados(turma):
    total = 0
    maior = 0

    for aluno in turma:
        total += aluno["Nota"]
        if aluno["Nota"] > maior:
            maior = aluno["Nota"]

    quantidade = len(turma)
    media = total / quantidade

    if media > 12:
        situacao = 'Boa'
    elif media < 9.5:
        situacao = 'Fraca'
    else:
        situacao = 'Razoável'

    print('\n--- Resultados da Turma ---')
    print('Quantidade de notas:', quantidade)
    print('Maior nota:', maior)
    print('Média da turma:', round(media, 2))
    print('Situação:', situacao)

    terminar = ''

    terminar = input('[S/N] Deseja adicionar mais alunos ? ').upper()
    while terminar != 'F' or terminar != 'V':
        terminar = input('[S/N] Deseja adicionar mais alunos ? ').upper()

    if terminar == 'S':
        adicionar(turma)
    elif terminar == 'N':
        print('Fim do Programa')
        exit()


def start():
    print('--- Análise de Alunos ---')
    turma = []

    adicionar(turma)

start()