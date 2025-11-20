turma = []
qtd_alunos = 5


for c in range(qtd_alunos):
    aluno = dict()  # ou {}

    aluno['Nome'] =  input(f'Digite o nome do {c+1}º aluno : ')
    aluno['Media'] = float(input(f'Digite a media do(a) {aluno['Nome']}: '))

    # Situaçao com OPERADOR TERNÁRIO
    aluno['Situaçao'] = 'Aprovado' if aluno['Media'] >= 9.5 else 'Reprovado'

    # Situação com IF normal
    '''
    if aluno['Media'] > 9.5:
        aluno['Situaçao'] = 'Aprovado'
    else:
        aluno['Situaçao'] = 'Reprovado'
    '''

    turma.append(aluno.copy())

print(turma)