import sqlite3

def conectar() :
    try:
        return sqlite3.connect('loja.db')
    except Exception as e:
        print(f'Erro ao iniciar a ligação a base de dados: {str(e)}')
        return ''

def criar_loja():
    conn = conectar()

    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS loja (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL,
            stock INTEGER
        )

    ''')
    conn.commit()
    conn.close()

criar_loja()