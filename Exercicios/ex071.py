
'''
Crie um programa que tenha uma função que receba um texto como parâmetro
e que mostre uma mensagem com tamanho adaptável.
'''

def texto(txt):
    tmnh = "-=" * (len(txt))

    print(tmnh + '-')
    print(f"{txt:^{len(tmnh) +1}}")
    print(tmnh + '-')

def menu():
    msg = input('Introduza um texto : ')
    texto(msg)

menu()