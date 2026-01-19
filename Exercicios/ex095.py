'''
Crie uma classe ContaBancaria com atributos privados
- nib,
- titular,
- saldo
- limite.
Adicione métodos getters e setters para os atributos.
'''

from random import randint

class Conta:
    def __init__(self):
        self.__nib = self.gerar_nib()
        self.__titular = input("Digite o nome do titular: ")
        self.__saldo = int(input("Digite o saldo inicial: "))
        self.__limite = 'limite'

    def gerar_nib(self):
        return ''.join(str(randint(0, 9)) for _ in range(23))

    def mostrar_dados(self):
        print("\n--- DADOS DA CONTA ---")
        print(f"NIB: {self.__nib}")
        print(f"Titular: {self.__titular}")
        print(f"Saldo: {self.__saldo}")
        print(f"Limite: {self.__limite}")


class ContaBancaria:
    def __init__(self):
        self.__nib = 'NIB'
        self.__titular = 'titular'
        self.__saldo = 'saldo'
        self.__limite = 500


conta = None

while True:
    print('[1] - Criar Conta')
    print('[2] - Visualizar Conta')
    print('[3] - Sair')

    opcao = int(input('Selecione uma opcao: '))

    if opcao == 1:
        conta = Conta()
        print('Conta criada com sucesso!\n')

    elif opcao == 2:
        if conta is None:
            print('Nenhuma conta criada ainda!\n')
        else:
            conta.mostrar_dados()

    elif opcao == 3:
        print('A sair do programa...')
        break

    else:
        print('Opcão Invalida!\n')
