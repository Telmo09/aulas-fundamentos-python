# Faça um programa que leia uma frase
# qualquer e diga se é um palíndromo,
# desconsiderando os espaços.

# Ex: Anotaram a data da maratona

frase = input('Insere uma frase : ').strip().lower()
frase_ns = frase.replace(' ', '')
reverse = frase[::-1]
reverse_ns = reverse.replace(' ', '')

if reverse_ns == frase_ns:
    print(f'A frase "{frase}" é um políndromo')
else:
    print(f'A frase "{frase}" não é um políndromo')
    print(f'{frase_ns}')
    print(f'{reverse_ns}')
