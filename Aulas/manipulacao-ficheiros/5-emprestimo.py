from datetime import datetime
from pathlib import Path

def cabecalho(txt: str) -> None:
    print(f'--- {txt.upper()} ---')

def busca_informacao() -> dict:
    dados  = dict()
    caminho = Path(r'ficheiros\dados.txt')
    with caminho.open('r', encoding='UTF-8', errors='ignore') as file:
        for linha in file:
            linha_dividida = linha.split(': ')
            dados[linha_dividida[0]] = linha_dividida[1].replace('\n', ' ')

    return dados

def calcula_informacao(dados: dict) -> dict:
    dados['MontanteCredito'] = float(input('Digite o Montante de Credito: '))
    dados['PrazoAnos'] = int(input('Indique o prazo, em anos: '))

    ano_atual = datetime.now().year

    dados['idade'] = ano_atual - dados['AnoNascimento']
    dados['remanescente'] = dados['RendimentoM'] - dados['DespesasM']
    dados['pgmtMensal'] = dados['MontanteCredito'] / (dados['PrazoAnos'] * 12)
    if dados['remanescente'] >= dados['pgmtMensal']:
        print(f'O crédito foi aprovado')
        print(f'O pagamento Mensal será de {dados['pgmtMensal']}€')
    else:
        print(f'O crédito não foi aprovado')
        print(f'O seu limite é de {dados['remanescente']}, e o pagamento seria de {dados['pgmtMensal']}')

    return dados

def guarda(dados: dict) -> str:
    caminho = Path(rf'ficheiros/{dados['Nome']}_resultados.txt')
    with caminho.open('w', encoding='UTF-8', errors='ignore') as file:
        for key, value in dados.items():
            file.write(f'{key}: {value}\n')

    return f'Resultado de {dados['Nome']} guardado com sucesso'

pessoa = calcula_informacao(busca_informacao())

