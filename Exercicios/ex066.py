'''
Crie um simulador de crédito habitação simples e sem taxas, que solicite :
- o nome,
- ano de nascimento,
- rendimentos mensais,
- despesas mensais,
- montante do crédito
- prazo em anos
guardando tudo dentro de um dicionário.

Calcule, acrescentando ao dicionário:
- a idade,
- o remanescente após despesas,
- quanto deverá pagar mensalmente pelo crédito
- e se o crédito foi aprovado sempre que o remanescente seja superior ao valor mensal do crédito.
'''

user = dict()

user['Nome'] = input('Digite o seu nome: ')
user['AnoNascimento'] = int(input('Digite o seu ano de Nascimento: '))
user['RendimentoM'] = int(input('Digite o valor do Rendimento Mensal: '))
user['DespesasM'] = int(input('Digite o valor das suas Despesas Mensais: '))
user['MontanteCredito'] = int(input('Digite o Montante de Credito: '))
user['PrazoAnos'] = int(input('Indique o prazo, em anos: '))

ano_atual = 2025
idade = ano_atual - user['AnoNascimento']
remanescente = user['RendimentoM'] - user['DespesasM']
pgmtMensal = user['MontanteCredito'] / (user['PrazoAnos']*12)

print(f'A idade do(a) {user['Nome']} é de {idade}')
print(f'O remanescente do(a) {user['Nome']} é de {remanescente}')

if remanescente >= pgmtMensal:
    print(f'O crédito foi aprovado')
    print(f'O pagamento Mensal será de {pgmtMensal}€')
else:
    print(f'O crédito não foi aprovado')
    print(f'O seu limite é de {remanescente}, e o pagamento seria de {pgmtMensal}')