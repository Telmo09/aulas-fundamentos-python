# Estabelecer a Ligação
# 1- Importar a biblioteca necessaria
import sqlite3

# 2- iniciar a conexao
def conectar() :
    try:
        return sqlite3.connect('tarefas.db')
    except Exception as e:
        print(f'Erro ao iniciar a ligação a base de dados: {str(e)}')
        return ''

# Criar uma tabela
def criar_tabela():
    conn = conectar() # criar conexão

    cursor = conn.cursor() # criar o cursor
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT NOT NULL,
            estado TEXT NOT NULL
        )
    
    ''')
    conn.commit()
    conn.close()

criar_tabela()

def cabecalho(txt: str) -> None:
    print(f'--- {txt} ---')

def adicionar_tarefa():
    print()
    cabecalho('ADICIONAR TAREFA')
    descricao_tarefa = input('Descriçao: ').strip()
    estado_tarefa = 'Pendente'

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO tarefas (descricao, estado) VALUES (?, ?)",
                   (descricao_tarefa, estado_tarefa))
    conn.commit()
    conn.close()
    print(f'Tarefa "{descricao_tarefa}" Adicionada com Sucesso !')
    input()


def ver_tarefas():
    print()
    cabecalho('MOSTRAR TAREFAS')
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tarefas")
    tarefas = cursor.fetchall()
    conn.close()

    for tarefa in tarefas:
        print('-----------------------------------------------------------------')
        print(f'ID: {tarefa[0]} | DESCRIÇAO: {tarefa[1]} | ESTADO: {tarefa[2]}')

    input()


def terminar_tarefa():
    print()
    cabecalho('TERMINAR TAREFA')
    id_tarefa = int(input('Digite o ID da tarefa: '))

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("UPDATE tarefas SET estado = ? WHERE id = ?",
                   ('Concluido', id_tarefa))

    conn.commit()
    conn.close()

    print('Tarefa Atualizada')
    input()


def apagar_tarefa():
    print()
    cabecalho('TERMINAR TAREFA')
    id_tarefa = int(input('Digite o ID da tarefa: '))

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM tarefas WHERE id = ?",
                   (id_tarefa,))

    conn.commit()
    conn.close()

    print('Tarefa apagada')
    input()


def menu():
    criar_tabela()
    while True:
        print('[ 1 ] - Adicionar Tarefa')
        print('[ 2 ] - Ver Tarefas')
        print('[ 3 ] - Concluir Tarefa')
        print('[ 4 ] - Apagar Tarefa')
        print('[ 5 ] - Sair do Programa')
        opcao = int(input('Selecione uma opção: '))

        match opcao:
            case 1:
                adicionar_tarefa()
            case 2:
                ver_tarefas()
            case 3:
                terminar_tarefa()
            case 4:
                apagar_tarefa()
            case 5:
                break
            case _:
                print('Opção Invalida...')

if __name__ == '__main__':
    menu()