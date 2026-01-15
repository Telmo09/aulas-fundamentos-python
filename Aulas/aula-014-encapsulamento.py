class Conta:
    def __init__(self):
        self.__titular = 'Ricardo'
        self.__saldo = 500.00
        self.__pin = '1234'
        self.__limite = 400.00

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, novo_titular):
        self.__titular = novo_titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @property
    def pin(self):
        return None

    def alterar_pin(self):
        pin_antigo = input('Digite o PIN antigo: ')
        if pin_antigo == self.__pin:
            novo_pin = input('Digite o novo PIN: ')
            repetir = input('Digite novamente o novo PIN: ')
            if novo_pin == repetir:
                self.__pin = novo_pin
                print('PIN alterado com sucesso.')
            else:
                print('PIN diferente.')
        else:
            print('PIN inválido.')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            return True
        return False

    def levantar(self, valor):
        if 0 < valor <= self.__limite and valor <= self.__saldo:
            self.__saldo -= valor
            return True
        return False


class ATM:
    def __init__(self, conta: Conta):
        self.conta = conta

    def depositar(self):
        valor = float(input('Valor a depositar: '))
        if self.conta.depositar(valor):
            print('Depósito efetuado com sucesso.')
        else:
            print('Valor inválido.')

    def levantar(self):
        valor = float(input('Valor a levantar: '))
        if self.conta.levantar(valor):
            print('Levantamento efetuado com sucesso.')
        else:
            print(f'Não é possível levantar mais de {self.conta.limite:.2f}€.')

    def mostrar_saldo(self):
        print(f'Saldo atual: {self.conta.saldo:.2f}€')

    def menu(self):
        while True:
            print('\n[1] Levantar')
            print('[2] Depositar')
            print('[3] Ver saldo')
            print('[4] Sair')
            opcao = input('---> ')

            if opcao == '1':
                self.levantar()
            elif opcao == '2':
                self.depositar()
            elif opcao == '3':
                self.mostrar_saldo()
            elif opcao == '4':
                print('Obrigado por usar o ATM.')
                break
            else:
                print('Opção inválida.')


if __name__ == '__main__':
    conta = Conta()
    atm = ATM(conta)
    atm.menu()
