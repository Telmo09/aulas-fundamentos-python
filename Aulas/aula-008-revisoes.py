'''numero = int(input('Digite um numero: '))

if numero > 10:
    print('Numero superior a 10')
elif numero == 10:
    print('Numero é 10')
else:
    print('Numero nao superior a 10')

for c in range(0, numero):
    print(c)

contador = 0

while True:
    print(contador)
    if contador == 10:
        break
    contador += 1'''

aluno = [1, 5, 7, 6, 3, 'Ricardo']
for indice, valor in enumerate(aluno):
    print(f'No indice {indice} tem o valor {valor}')
