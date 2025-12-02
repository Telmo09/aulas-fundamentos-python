# classe Path que da metodos/funçoes tipicas de ficheiro
from pathlib import Path

'''
string = r'ola\nola' # ignora \n
print(string)
'''

# informar qual é o caminho do ficheiro
# Criar a Variavel que representa o caminho do ficheiro
caminho = Path(r'ficheiros/teste.txt')
print('Caminho criado com sucesso')

# O Python cria o ficheiro se ele não existir
# Podemos abrir o ficheiro em modos diferentes:
# - Write - 'w' (escrever)
# - Read - 'r' (ler)
# - Append - 'a' (acrescentar)

with caminho.open('w', encoding='utf-8', errors='ignore') as file:
    print('Ficheiro aberto com sucesso')
    file.write('Ola Turma \n')
    file.write('Ola Novamente')
    file.write('FansFans')
    print('Mensagem Escrita com sucesso')