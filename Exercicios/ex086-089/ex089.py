import sqlite3


def conectar_db():
    return sqlite3.connect('loja.db')

def criar_tabela():
    conn = conectar_db()
    cursor = conn.cursor()

    query = '''
        CREATE TABLE IF NOT EXISTS loja (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL,
            stock INTEGER
        )

    '''

    cursor.execute(query)
    conn.commit()
    conn.close()

def adicionar_produto_db(nome: str, preco: float, stock: int) -> None:
    conn = conectar_db()
    cursor = conn.cursor()

    cursor.execute('INSERT INTO produto (nome, preco, stock) VALUES (?, ?, ?)',
                   (nome, preco, stock))

    conn.commit()
    conn.close()


