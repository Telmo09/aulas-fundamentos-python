import sqlite3

def conectar() :
    try:
        return sqlite3.connect('loja.db')
    except Exception as e:
        print(f'Erro ao iniciar a ligação a base de dados: {str(e)}')
        return ''


def alteracao_preco():

    conn = conectar()
    cursor = conn.cursor()

    produto_confirm = ''
    while produto_confirm != 'S':
        id_produto = int(input('Digite o ID do produto: '))

        cursor.execute('SELECT * FROM loja WHERE id = ?', (id_produto,))
        produto = cursor.fetchone()

        print(f'Produto: {produto[1]}')
        print(f'Preço: {produto[2]}')
        print(f'Stock: {produto[3]}')
        print()

        produto_confirm = input('[S/N] Confirma ser este o produto ? ')

        if produto_confirm == 'S':
            break

    print()

    change = ''
    while change != 'S':
        novo_preco = float(input('Indique o novo preco: '))

        change = input('[S/N] Confirma alteração ? ').upper()

        if change == 'S':
            cursor.execute("UPDATE loja SET preco = ? WHERE id = ?",
                           (novo_preco, id_produto))
            break
        else:
            continue

    conn.commit()
    conn.close()

    print()
    print('Preço Alterado com sucesso')


def start():
    print('--- Alteração de Preços ---')
    print()
    alteracao_preco()

start()