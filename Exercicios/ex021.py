# Crie um programa que leia uma frase e mostre:
# ✓ Quantas vezes aparece a letra “A”;
# ✓ Em que posição aparece a primeira vez;
# ✓ Em que posição aparece a última vez.

frase = input('Escreva uma frase : ').strip()

qtd_a = frase.count('A')
print(f'O A aparece {qtd_a} vezes')

p_posicao = frase.find('A')
print(f'Aparece pela primeira vez na posiçao {p_posicao + 1}.')

u_posicao = frase.rfind('A')
print(f'Aparece pela ultima vez na posição {u_posicao + 1}')

# --------------------------------------------

print(frase.count('A')) # quantos A
print(frase.find('A')) # aparecer primeira vez
print(int(len(frase)) - int((frase[::-1].find('A')))) # aparece ultima vez