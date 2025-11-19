# Crie um programa onde o utilizador insira 5 números dentro de uma lista.
# Os valores devem ser registados já na posição correta [ordem crescente]
# e no final mostre a lista ordenada.

lista = list()

for c in range(0, 5):
    addnum = int(input(f'[{c + 1}/5] Introduza um número: '))
    for indice, numero in enumerate(lista):
        if numero > addnum:
            lista.insert(indice, addnum)
            break
    else:
        lista.append(addnum)
    print(lista)