# estante = input('Digite uma consola : '), input('Digite outra consola : ')

nomes = ('Nadia', 'Julia', 'Alexandra', 'Telmo',
         'Viktor', 'Rafael', 'Daniel', 'Leticia',
         'Roman', 'Pedro', 'Franchika', 'Inês',)

'''TAM = len(nomes)

for c in range(0, TAM):
    print(f'No indice {c} está o nome {nomes[c]}')

contador = 0
for nome in nomes:
    print(f'No indice {contador} está o nome {nomes[contador]}')
    contador += 1'''

'''for c in range(0, len(nomes)):
    print(f'{c+1} -> {nomes[c]}')'''

'''for nome in nomes:
    if nome == 'Roman':
        print(nome)'''

for indice, nome in enumerate(nomes):
    if indice % 2 == 0:
        print(f'No indice {indice} o valor é {nome}')

print(type(nomes))