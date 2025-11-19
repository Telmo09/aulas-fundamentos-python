# contador que vai de 1 até 10
'''contador = 1

while contador <= 10:
    print(contador)
    contador += 1'''

# contador que vai de 10 até o 0
'''contador = 10

while contador >= 0:
    print(contador)
    contador -= 1'''

# criar um programa que some todos os numeros digitados pelo utilizador
# quantos? Nao se. Só sei que se o utilizador digitar 0, é para parar

'''soma = 0
numero = ''

while numero != 0:
    numero = int(input('Digite um numero : '))
    soma += numero

print(soma)'''

# Eu quero criar um programa que peça o género de uma pessoa
# Apenas aceitar como resposta 'M' ou 'F'
# Se o utilizador digitar outra resposta ele vai ter de pedir novamente

'''genero = ' '
while genero != 'M' and genero != 'F':
    genero = input('Digite o seu género : ').strip().upper()'''

# Quero criar um menu onde o utilizador pode esclher 3 opções :
# Escrever 'ola' , 'tudo bem ?' , 'sair do programa.

'''opcao = ''
while opcao !=3:
    print('--- MENU ---')
    print('[1] - Olá')
    print('[2] - Tudo bem ?')
    print('[3] - Sair')
    opcao = int(input('--->'))

    if opcao == 1:
        print('Olá')
    elif opcao == 2:
        print('Tudo bem?')
    elif opcao ==3:
        print('A sair ...')
    else:
        print('Opção inválida')'''

'''while True:
    print('--- MENU ---')
    print('[1] - Olá')
    print('[2] - Tudo bem ?')
    print('[3] - Sair')
    opcao = int(input('---> '))

    if opcao == 1:
        print('Olá')
    elif opcao == 2:
        print('Tudo bem?')
    elif opcao ==3:
        print('A sair ...')
        break
    else:
        print('Opção inválida')'''

# contagem de 0 até 1000

contador = 0

while True:
    print(contador)
    contador += 1

    if contador == 1000:
        print(1000)
        break

