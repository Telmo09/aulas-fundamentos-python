# Crie um programa onde o utilizador possa digitar vários números e guardá-los numa lista.
# Caso o número inserido esteja na lista ele não deve ser adicionado.
# No final mostre todos os valores por ordem DECRESCENTE.

lista = list()
print('Se colocar um número repetido, o codigo pára')

while True:
    addnum = int(input('Insere um numero : '))

    if addnum == 0:
        break

    repetido = False
    for indice, numeros in enumerate(lista):
        if numeros == addnum:
            print('- Numero já foi introduzido')
            repetido = True

    if repetido:
        break
    else:
        print(f'{addnum} foi adicionado com sucesso')
        lista.append(addnum)


crescente = sorted(lista)
decrescente = sorted(lista, reverse=True)
print('--- Terminando ---')
print(crescente)
print(f'Numeros colocados : {decrescente}')