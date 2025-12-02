import os

# nome_pasta = 'fans/ficheiros'
# os.mkdir(nome_pasta)

caminho = 'fans/ficheiros'
os.makedirs(caminho, exist_ok=True)

# Diferenças :
# O primeiro so cria 1 ficheiro
# O segundo pode cria varios
# O primeiro da erro se ja existir
# O segundo ignora se ja existir (nao gera erro)
