# Crie um programa que leia o nome completo de uma pessoa e mostre:
# ✓ O nome com todas as letras maiúsculas;
# ✓ O nome com todas as letras minúsculas;
# ✓ Quantidade de letras sem espaços;
# ✓ Quantas letras tem o primeiro nome.

nome = input('Indique o seu nome : ').strip()

print(nome.upper()) # tudo maiusculo
print(nome.lower()) # tudo minusculo
qtd_espacos = nome.count(' ') # conta quantos espaços existem
print(len(nome) - qtd_espacos) # mostra qtd caracteres - qtd espaços
print(len(nome.replace('',''))) # mostra qtd caracteres sem espaços

pEspaço = nome.find(' ') # encontro o indice do primeiro espaço
print(nome[:pEspaço]) # imprimir string do inicio ate o fim do primeiro espaço