from math import  fsum

'''notas = list()

print(type(notas))

for c in range(0, 5):
    nota = float(input(f'Digite a {c+1} nota : '))
    notas.append(nota)

media = fsum(notas) / len(notas)
print(media)'''

'''nomes = ['Nadia', 'Julia', 'Alexandra', 'Telmo',
         'Viktor', 'Rafael', 'Daniel', 'Leticia',
         'Roman', 'Pedro', 'Franchika', 'Inês']

print(nomes)
nomes.append('João') #adiciona o joao no fim
print(nomes)
nomes.insert(0, 'Luanna') # adiciona Luanna no inicio e puxa tudo a direita
print(nomes)

nomes.pop() # tira o ultimo (joao)
print(nomes)'''

series = list()

print('insere o teu top 5 de series')
for c in range(0, 5):
    serie = input(f'{c+1}º --> ')
    series.append(serie)

    print(series)

while True:
    print()
    print('[1] - Inserir novo top 5')
    print('[2] - Substituir série')
    print('[3] - Mostrar top 5')
    print('[4] - Sair')
    print()
    opcao = int(input('--> '))
    match opcao:
        case 1:
            print('insere o teu top 5 de series')
            for c in range(0, 5):
                serie = input(f'{c + 1}º --> ')
                series.append(serie)
        case 2:
            nova_serie = input('Digite a nova serie : ')
            serie_remover = input('Digite a serie a remover : ')

            indice_serie_remover = series.index(serie_remover)

            series[indice_serie_remover] = series.index(serie_remover)
            print('Serie alterada com sucesso !')

        case 3:
            for indice, serie in enumerate(series):
                print(f'{indice+1} -> {serie}')

        case 4:
            print('A Sair ...')
            break

        case _:
            print('Opção Invalida')