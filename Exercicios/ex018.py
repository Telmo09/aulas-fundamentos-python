#Crie um programa que pergunte a
#quantidade de km percorridos por um
#carro alugado e quantidade de dias que
#foi alugado. Apresente o total a pagar
#sabendo que o carro custa 60€/dia e
#0.456€/km.

from time import sleep

kms = int(input('Quantos kilometros foram percorridos ? '))
dias = int(input('Quantos dias foram alugados ? '))

custokms = kms * 0.456
custodias = dias * 60
custototal = custodias + custokms

sleep(1)
print('A calcular custos', end='')

sleep(1)
print('.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.', end='\n')

sleep(1)

print('Custo total :', custototal, '€')