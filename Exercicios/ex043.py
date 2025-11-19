# Desenvolva um programa que leia 3 valores e mostre o menu:
# [1] SOMAR
# [2] MULTIPLICAR
# [3] MAIOR
# [4] NOVOS NÚMEROS
# [5] SAIR DO PROGRAMA
# O programa deve realizar a operação solicitada em cada caso.

opcao = ''
maior = ''

while opcao !=5:
    num1 = int(input('Introduza o 1º numero : '))
    num2 = int(input('Introduza o 2º numero : '))
    num3 = int(input('Introduza o 3º numero : '))

    opcao = ''

    while opcao != 4:
        print('[1] - SOMAR')
        print('[2] - MULTIPLICAR')
        print('[3] - MAIOR')
        print('[4] - NOVOS NÚMEROS')
        print('[5] - SAIR DO PROGRAMA')
        opcao = int(input('Escolha uma opção : '))
        print(f'Numeros usados foram : {num1} , {num2} , {num3}')

        if opcao == 1:
            soma = num1 + num2 + num3
            print(f'Soma Total é de {soma} !')
            print()
        elif opcao == 2:
            mult = num1 * num2 * num3
            print(f'A multiplicação dos números é de {mult}')
            print()
        elif opcao == 3:
            maior_num = num1
            if num2 > maior_num:
                maior_num = num2
            if num3 > maior_num:
                maior_num = num3
            print(f'O maior numero é {maior_num}')
            print()
        elif opcao == 4:
            num1 = ''
            num2 = ''
            num3 = ''
            maior_num = ''
            print('--- RESET ---')
            print('Escolha novos numeros')
            print()
        elif opcao == 5:
            print('A sair ...')
            print()
            break
        else:
            print('Opção inválida')
            print()

print('Fim do programa')