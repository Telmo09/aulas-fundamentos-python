from random import randint

estrelas = []

for c in range(0,100):
    for a in range(0, 2):  # sao 2 estrelas
        while True:
            num = randint(1, 12)
            if num in estrelas:  # verificar se ja tem
                continue  # repetir ate sair diferente
            else:  # apenas inclui se nao houver repetido
                estrelas.append(f'{num}*')  # acrescentar a estrela (com *)
                break  #

    print(estrelas)
    estrelas = []