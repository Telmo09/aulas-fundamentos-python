def imccalc(peso, altura):
    imc = peso / (altura * altura)
    return imc

def inicio():
    print('--- Calculo de IMC ---')
    nome = input('Indique o seu nome: ')
    peso = float(input(f'{nome}, indique o seu peso: '))
    altura = float(input(f'{nome}, indique a sua altura: '))

    imc = imccalc(peso, altura)
    final(nome, imc)

def final(nome, imc):
    from pathlib import Path
    caminho = Path(r'imc.txt')

    print(f'O IMC de {nome} é de {imc:.2f}')

    with caminho.open('a', encoding='UTF-8', errors='ignore') as file:
        file.write(f'Nome : {nome} | IMC : {imc:.2f}' + '\n')

    cont = ''
    while cont != 'S' and cont != "N":
        cont = input('[S/N] Deseja adicionar mais ? ').upper()

    if cont == 'S':
        inicio()
    elif cont == 'N':
        exit()

inicio()