# Desenvolva um programa em python, de acordo com todas
# as boas práticas aprendidas, que simule um bloco de notas.

# O programa deve permitir:
# 1. Adicionar notas a um ficheiro .txt;
# 2. Mostrar todas as notas gravadas;
# 3. Apagar todas as notas;
# 4. Pesquisar notas por palavra-chave.
# No final coloque o projeto no GitHub

# Projeto de grupo
# Elementos do grupo: Telmo, Francisca, Victor

from time import sleep
from pathlib import Path


def adicionar(caminho):
    print('\n--- Adicionar Nova Nota ---')
    nota = input('Digite sua nota: ')
    with caminho.open('a', encoding='utf-8', errors='ignore') as file:
        file.write(nota + '\n')
    print('Nota adicionada com sucesso!')


def ler(caminho): # TERMINADO | NÃO ALTERAR
    with caminho.open('r', encoding='UTF-8', errors='ignore') as file:
        for linha in file:
            print(linha, end='')
            print('Leitura Concluida !')

def apagar(caminho): # TERMINADO | NÃO ALTERAR
    with caminho.open('w', encoding='utf-8', errors='ignore') as file:
        file.write('')
        print('Ficheiro apagado com sucesso')


def pesquisa(caminho):
    saida = Path(r'notas_copia.txt')

    print('Procura de palavra chave')
    palavra: str = input('Digite uma palavra: ')

    with caminho.open('r', encoding='UTF-8', errors='ignore') as file:
        dados = file.readlines()

    with saida.open('w', encoding='UTF-8', errors='ignore') as out:
        for linha in dados:
            if palavra in linha.lower():
                out.write(linha)

    with saida.open('r', encoding='UTF-8', errors='ignore') as file:
        for linha in file:
            print(linha, end='')


def main():
    caminho = Path(r'projeto4_bloco_de_notas.txt')
    print('Caminho criado com sucesso')

    for c in range(1,5):
        while True:
            print('\n\nº*~º*~ Bloco de Notas ~*º~*º')
            print('[ 1 ] - Escrever Conteúdo')
            print('[ 2 ] - Ler')
            print('[ 3 ] - Apagar')
            print('[ 4 ] - Pesquisar')
            print('[ 5 ] - Sair')
            opcao = int(input('Selecione uma opção -> '))

            if opcao == 1: #adicionar conteúdo
                adicionar(caminho)
            elif opcao == 2: # ler o bloco de notas
                ler(caminho)
            elif opcao == 3: # limpar o Bloco de Notas
                apagar(caminho)
            elif opcao == 4: # Pesquisar por termos específicos
                pesquisa(caminho)
            elif opcao == 5: # Fim do Programa
                print('A sair...\n')
                sleep(0.5)
                break
            else:
                print('Por favor selecione uma opção valida!\n')

main()

################
# anotaçoes
