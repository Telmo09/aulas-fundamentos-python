aluno = dict()

aluno['Nome'] =  input(f'Digite o nome do aluno : ')
aluno['Media'] = float(input(f'Digite a media do(a) {aluno['Nome']}: '))

aluno['Situaçao'] = 'Aprovado' if aluno['Media'] >= 9.5 else 'Reprovado'
print(f'{aluno['Nome']} foi {aluno['Situaçao']}')

print(aluno)

for chave, valor in aluno.items():
    print(f'{chave} -> {valor}')