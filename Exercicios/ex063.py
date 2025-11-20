from random import randint
from time import sleep

sorteio = list()
numeros_euromilhoes = list()
estrelas_euromilhoes = list()

repetir = int(input("Quantas chaves deseja gerar ? "))
sleep(0.7)
print("A gerar chaves ... ")

for r in range(0,repetir):
    for numeros in range(0,5): # sao 5 numeros
        while True:
            num = randint(1, 50)
            if num in numeros_euromilhoes: # verificar se ja tem
                continue # repetir ate sair diferente
            else: #apenas inclui se nao houver repetido
                numeros_euromilhoes.append(num) # acrescentar o numero
                break # correto , avança para o proximo

    for estrelas in range(0, 2): # sao 2 estrelas
        while True:
            num = randint(1, 12)
            if num in estrelas_euromilhoes: # verificar se ja tem
                continue # repetir ate sair diferente
            else: #apenas inclui se nao houver repetido
                estrelas_euromilhoes.append(f'{num}*') # acrescentar a estrela (com *)
                break # correto , avança para o proximo

    sorteio.append(sorted(numeros_euromilhoes))
    sorteio.append(sorted(estrelas_euromilhoes))

    sleep(1)
    print(f'[Euromilhoes {r+1}] - Numeros, Estrelas')
    sleep(0.3)
    print(sorteio)
    print()

    sorteio = list()
    numeros_euromilhoes = list()
    estrelas_euromilhoes = list()