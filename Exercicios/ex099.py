class Conta:
    def __init__(self):
        self.__nib = self.gerar_nib()
        self.__titular = input("Digite o nome do titular: ")
        self.__saldo = int(input("Digite o saldo inicial: "))
        self.__limite = 'limite'

    def gerar_nib(self):
        from random import randint
        return randint(100000000, 999999999)

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, novo_titular):
        self.__titular = novo_titular

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, novo_saldo):
        if novo_saldo < 0:
            print("Saldo não pode ser negativo!")
        else:
            self.__saldo = novo_saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    @property
    def nib(self):
        return self.__nib

    def depositar(self):
        valor = float(input('Valor a Depositar: '))
        self.__saldo += valor

    def sacar(self):
        valor = float(input('Valor a Sacar: '))
        if valor > self.__limite or self.__saldo - valor < 0:
            print('ERRO NO LEAVANTAMENTO')
        else:
            self.__saldo -= valor

