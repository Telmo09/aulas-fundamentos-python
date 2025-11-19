# Crie um programa que leia um número de 0 a 20 introduzido pelo utilizador.
# Depois deverá mostrar por extenso o número introduzido.

numeros = ('Zero', 'Um', 'Dois', 'Tres',
         'Quatro', 'Cinco', 'Seis', 'Sete',
         'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
         'Treze', 'Quatorze','Quinze', 'Dezasseis',
         'Dezassete', 'Dezoito', 'Dezanove', 'Vinte')

print('--- COMO SE ESCREVER OS NUMEROS ---')
user = int(input('Introduz um numero : '))

for c in range(0, 21):
    if c == user:
        print(f'O numero {c} por extenso é : {numeros[c]}')
