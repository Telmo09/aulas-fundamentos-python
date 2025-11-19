# Projeto 3 :
# - Telmo
# - Nadia
# - Julia

opcao = 0

while opcao != 5:
    print('\n--- Desenhador de Formas ---')
    print('[1] - Escadas para a esquerda')
    print('[2] - Escadas para a direita')
    print('[3] - Piramide')
    print('[4] - Crux (X)')
    print('[5] - Sair')
    opcao = int(input('Selecione uma opção : '))

    if opcao == 1:
        for a in range(1, 6):
            print('*' * a)
    elif opcao == 2:
        for b in range(1, 6):
            espacos1 = ' ' * (5 - b)
            print(espacos1 + '*' * b)
    elif opcao == 3:
        for c in range(1, 6):
            espacos2 = ' ' * (5 - c)
            stars = "*" * (2 * c - 1)
            print(f'{espacos2} {stars}')
    elif opcao == 4:
        for linha in range(5):
            for coluna in range(5):
                if linha == coluna or linha + coluna == 4:
                    print('*', end='')
                else:
                    print(' ', end='')
            print()
    elif opcao == 5:
        break
    else:
        print('Opção inválida !')

print('Fim do Programa')