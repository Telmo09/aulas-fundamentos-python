# --- Calculadora ---
# [ 1 ] – Tabuada
# [ 2 ] – Calculadora
# [ 3 ] – Números Pares
# [ 4 ] – Sair
#
# Mediante a opção solicitada o sistema
# deve executar a ação do menu.

print('--- Calculadora---')
print('[ 1 ] – Tabuada')
print('[ 2 ] – Calculadora')
print('[ 3 ] – Números Pares')
print('[ 4 ] – Sair')

opcao = int(input('Escolha uma opção : '))

if opcao == 1:
    print('Escolheu a Tabuada !')
    tabuada = int(input('Escolha um número : '))
    print(f'{tabuada} x 1 = {tabuada*1}')
    print(f'{tabuada} x 2 = {tabuada*2}')
    print(f'{tabuada} x 3 = {tabuada*3}')
    print(f'{tabuada} x 4 = {tabuada*4}')
    print(f'{tabuada} x 5 = {tabuada*5}')
    print(f'{tabuada} x 6 = {tabuada*6}')
    print(f'{tabuada} x 7 = {tabuada*7}')
    print(f'{tabuada} x 8 = {tabuada*8}')
    print(f'{tabuada} x 9 = {tabuada*9}')
    print(f'{tabuada} x 10 = {tabuada*10}')

elif opcao == 2:
    print('Escolheu a Calculadora')
    calc1 = int(input('Digite um número : '))
    oper = input('[+ - * / ?] ')
    calc2 = int(input('Digite outro número : '))
    if oper == '+':
        print(f'{calc1} + {calc2} = {calc1 + calc2}')
    if oper == '-':
        print(f'{calc1} - {calc2} = {calc1 - calc2}')
    if oper == '*':
        print(f'{calc1} * {calc2} = {calc1 * calc2}')
    if oper == '/':
        print(f'{calc1} / {calc2} = {calc1 / calc2}')

# calculo = input('Digite o calculo: ')
# if '+' in calculo:
#     pos = calculo.find('+')
#     num1 = int(calculo[:pos])
#     num2 = int(calculo[pos+1:])
#     print(f'{num1} + {num2} = {num1 + num2}')
# if '-' in calculo:
#     pos = calculo.find('-')
#     num1 = int(calculo[:pos])
#     num2 = int(calculo[pos+1:])
#     print(f'{num1} - {num2} = {num1 - num2}')
# if '*' in calculo or 'x' in calculo:
#     if 'x' in calculo
#         pos = calculo.find('x')
#         num1 = int(calculo[:pos])
#         num2 = int(calculo[pos+1:])
#         print(f'{num1} x {num2} = {num1 * num2}')
#     if '*' in calculo
#     pos = calculo.find('*')
#     num1 = int(calculo[:pos])
#     num2 = int(calculo[pos+1:])
#     print(f'{num1} x {num2} = {num1 * num2}')
# if '/' in calculo:
#     pos = calculo.find('-')
#     num1 = int(calculo[:pos])
#     num2 = int(calculo[pos+1:])
#     if num2 == 0
#         print('Não é possivel dividir por 0')
#     else
#         print(f'{num1} / {num2} = {num1 / num2}')'''

elif opcao == 3:
    print('Escolheu : Numeros Pares')
    num = int(input('Insere um número : '))
    # numeros pares : 0 2 4 6 8
    # numeros impares : 1 3 5 7 9
    if num % 2 == 0:
        print(f"O número {num} é par.")
    else:
        print(f"O número {num} é ímpar.")

elif opcao == 4:
    print('Adeus')

else:
    print('Error 404 : not found')

