import sqlite3

def conectar() :
    try:
        return sqlite3.connect('loja.db')
    except Exception as e:
        print(f'Erro ao iniciar a ligação a base de dados: {str(e)}')
        return ''

def quantificacao():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM loja")
    quantidade = cursor.fetchone()[0]

    conn.close()

    adicionar_produto(quantidade)

def adicionar_produto(quantidade):
    print()

    print(f'Atualmente existe {quantidade} produtos da database')

    nome_produto = input('Nome do produto: ').strip()
    preco_produto = float(input(f'Qual o preço de "{nome_produto}" ? '))
    stock_produto = int(input(f'Quanto há em stock de "{nome_produto}" ? '))

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO loja (nome, preco, stock) VALUES (?, ?, ?)",
                   (nome_produto, preco_produto, stock_produto))
    conn.commit()
    conn.close()

    print()
    print(f'Produto : {nome_produto}')
    print(f'Preço : {preco_produto}')
    print(f'Stock : {stock_produto}')
    print(f'Adicionado com sucesso')
    print()
    repeticao(quantidade)


def repeticao(quantidade):

    print(f'Atualmente existe {quantidade+1} produtos da database')
    repetir = ''
    while repetir != 'S' and repetir != 'N':
                repetir = input('[S/N] Deseja adicionar mais produtos ? ').upper()

    if repetir == 'S':
        quantificacao()
    elif repetir == 'N':
        print('Programa Terminado !')
        exit()

def start():
    print('--- Criação de Stock ---')
    print('Vamos adicionar produtos')
    quantificacao()

start()
