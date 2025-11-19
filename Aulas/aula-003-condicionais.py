limite_velocidade = 120
minimo_velocidade = 50

print('--- RADAR DE VELOCIDADE ---')

velocidade = int(input('---> '))

if velocidade > limite_velocidade:
    print('MULTADO !')
elif velocidade < minimo_velocidade:
    print('Acelera Moço !')
else:
    print('Boa Viagem !')

print('Fim do Programa!')
