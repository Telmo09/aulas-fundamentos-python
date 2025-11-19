# Escreva um programa que leia um número N inteiro qualquer e mostre os N
# primeiros elementos de uma sequência de Fibonacci.

# 0 1 1 2 3 5 8 13 21

from time import sleep

antecessor = 0  # atrbui o primeiro valor da sequencia
atual = 1  # atribui o segundo valor da sequencia
print('--- Sequencia de Fibonacci ---')
sequencia = int(input('Digite um valor: ')) #peço ao utilizador quantas vezes quer ver a sequencia

if sequencia <1: # se mostrar inferior a 1, ele diz valor invalido
    print('Valor Invalido:')
elif sequencia == 1: # se a sequencia for 1, ele mostra o primeiro valor da sequencia
    print(antecessor)
elif sequencia == 2: # se a sequencia for 2, ele mostra os 2 primeiros valores
    print(f'{antecessor} -> {atual}')
else:
    print(f'{antecessor} -> {atual}', end=' ')
    sequencia = sequencia - 2 #enquanto a sequencia for superior ou igual a 2, ele repete

    while sequencia >= 1:
        sucessor = antecessor + atual # calcula o valor seguinte aos dois primeiros
        print(f'-> {sucessor}', end=' ') # mostra esses valores calculado
        antecessor = atual # transfere os valores
        atual = sucessor # transfere os valores
        sleep(0.1)

        sequencia -=1 # retira 1 á sequencia