'''
Crie uma classe ContaBancaria com atributos titular, saldo e limite.
Adicione métodos para depositar() e sacar(),
alterando o saldo da conta de acordo com a operação.
'''

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self.limite = 100

    def depositar(self, deposito):
        saldoanterior = self.saldo
        self.saldo += deposito
        print(f'\nSaldo alterado de {saldoanterior} para {self.saldo}\n')

    def sacar(self, sacar):
        if sacar > self.limite:
            print('Valor Invalido, atingiu o limite !')
        else:
            saldoanterior = self.saldo
            self.saldo -= sacar
            print(f'\nSaldo alterado de {saldoanterior} para {self.saldo}\n')

Conta1 = ContaBancaria('Telmo', 5000)

def start():
    while True:
        print('--- MENU ---')
        print('[1] - Depositar')
        print('[2] - Levantar')
        print('[3] - Sair')
        opcao = int(input('Selecione uma opçao: '))

        if opcao == 1:
            deposito = int(input('Indique quanto quer depositar: '))
            ContaBancaria.depositar(Conta1, deposito)
        elif opcao == 2:
            sacar = int(input('Indique quanto quer levantar: '))
            ContaBancaria.sacar(Conta1, sacar)
        elif opcao == 3:
            break
        else:
            print('Opcao Invalida !')

start()
