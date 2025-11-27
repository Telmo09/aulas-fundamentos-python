
'''
def some(numero1: int, numero2: int):
    s = numero1 + numero2
    print(f'A soma deu {s}')
    return s

resultado = soma(numero1: 5, numero2: 5)
'''

def soma_numeros(lista: list) -> int:
    soma = 0

    # print(notas) ->

    for numero in lista:
        soma += numero

    return soma

notas = [20,20,20,20,20]

media = soma_numeros(notas) / len(notas)

print(media)
# print(soma) nao executa pq nao esta dentro do def