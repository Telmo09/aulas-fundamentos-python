# Crie um programa que leia um número inteiro introduzido pelo utilizador e
# que simule um radar de velocidade.

# >80km/h multado
# <=80km/h não multado

# A multa são 100€ + 7€ por cada km/h acima

print('--- RADAR DE VELOCIDADE')
velocidade = int(input('Inserir Velocidade : '))

limite_velocidade = 80

multa = 100
multa_extra = (velocidade - 80) * 7
multatotal = multa + multa_extra

if velocidade <= limite_velocidade:
    print('Não Multado')
elif velocidade > limite_velocidade:
    print('Multado !')
    print(f'Custo da multa : {multatotal:.2f}€')