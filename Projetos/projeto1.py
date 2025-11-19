# Desenvolva um programa em Python que permita ao
# utilizador calcular o seu Índice de Massa Corporal
# (IMC). O programa deve solicitar ao utilizador a sua
# altura e o seu peso. De seguida, deve calcular o IMC e o
# programa deve exibir uma mensagem com base no valor do
# IMC calculado.
# ● IMC abaixo de 18,5: Abaixo do peso
# ● IMC entre 18,5 e 24,9: Peso normal
# ● IMC entre 25,0 e 29,9: Sobrepeso
# ● IMC entre 30,0 e 34,9: Obesidade grau 1
# ● IMC entre 35,0 e 39,9: Obesidade grau 2
# ● IMC acima de 40,0: Obesidade grau 3 (obesidade mórbida)

print('--- Calculo do IMC ---')
peso = float(input('Qual é o seu peso ? '))
altura = float(input('Qual é a sua altura (em cm)? ')) / 100

imc = peso / (altura * altura)

if imc < 18.5:
    print(f'O seu IMC é de {imc:.2f}')
    print('Abaixo do peso')
elif imc < 24.9:
    print(f'O seu IMC é de {imc:.2f}')
    print('Peso Normal')
elif imc < 29.9:
    print(f'O seu IMC é de {imc:.2f}')
    print('Sobrepeso')
elif imc < 34.9:
    print(f'O seu IMC é de {imc:.2f}')
    print('Obesidade grau 1')
elif imc <39.9:
    print(f'O seu IMC é de {imc:.2f}')
    print('Obseidade grau 2')
else:
    print(f'O seu IMC é de {imc:.2f}')
    print('Obesidade grau 3')