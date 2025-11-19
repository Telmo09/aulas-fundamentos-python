# Crie um programa que leia vários números e coloca-os numa lista.
# Crie duas listas adicionais que vão conter os números pares e impares da lista principal.
# No final mostre todas as listas.

lista_inicial = list()
lista_pares = list()
lista_impar = list()

print('Se o numero for 0, o programa para !')

while True:
    num = int(input('Adicione um numero : '))
    if num == 0 :
        break
    lista_inicial.append(num)
    if num % 2 == 0 :
        lista_pares.append(num)
    if num % 2 == 1 :
        lista_impar.append(num)

print()
print('Os numeros inseridos foram os seguintes :')
print(lista_inicial)
print()
print('Dos quais :')
print(f'Pares :{lista_pares}')
print(f'Impares : {lista_impar}')