try:
    num1 = int(input('Digite um numero: '))
    num2 = int(input('Digite outro numero: '))

    divisao = num1/num2

except ZeroDivisionError:
    print('Não é possivel dividir por Zero.')

except ValueError:
    print('Por favor digite um numero valido.')

except KeyboardInterrupt:
    print('O utilizador encerrou o programa')

else:
    print(f'{num1} / {num2} = {divisao}')

finally:
    print('Programa encerrado')