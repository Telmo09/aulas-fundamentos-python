string = 'Python é Poderoso'

# Fatiamento de strings / string slicer
print(string[7]) # é
print(string[-1]) # ultimo caracter
print(string[:6]) # Python
print(string[9:]) # Poderoso
print(string[::2]) # do inicio ao fim de 2 em 2
print(string[::-1]) # mostra a string ao contrario

# Analise de strings / String Analisys
print(len(string)) # tamanho da string
print(string.count('o')) # quantas vezes aparece o "o"
print('Python' in string) # devolve true ou false
print(string.find('é')) # devolve a posiçao do solicitado
print(string.find('Olé')) # não encontra e devolve -1
print(string.startswith('Python')) # devolve true ou false
print(string.endswith('Fraquinho')) # devolve true ou false

# Transpormação de String / String Transfiguration
string = input('Digite uma frase: ')

print(len(string)) # contar
print(len(string.strip())) # tirar espaços
print(len(string.rstrip())) # retirar espaços a direita
print(string.lower()) # tudo minusculo
print(string.upper()) # tudo maiusculo
print(len(string.replace(' ','')))