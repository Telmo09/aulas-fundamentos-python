# Desenvolva um programa que faça 3
# perguntas ao utilizador e apenas
# aceite como resposta “V” ou “F”. Caso
# esteja errado, peça para repetir a
# resposta até ter um valor correto.

pergunta1 = ' '
while pergunta1 != 'V' and pergunta1 != 'F':
    pergunta1 = input('[V/F] O céu é azul ? ').strip().upper()
    if pergunta1 == 'V':
        print('Acertou !')
    elif pergunta1 == 'F':
        print('Errou !')
    else:
        print('Resposta Invalida')

pergunta2 = ' '
while pergunta2 != 'V' and pergunta2 != 'F':
    pergunta2 = input('[V/F] Japão fica na Asia ? ').strip().upper()
    if pergunta2 == 'V':
        print('Acertou !')
    elif pergunta2 == 'F':
        print('Errou !')
    else:
        print('Resposta Invalida')

pergunta3 = ' '
while pergunta3 != 'V' and pergunta3 != 'F':
    pergunta3 = input('[V/F] O formador é o Ricardo ? ').strip().upper()
    if pergunta3 == 'V':
        print('Acertou !')
    elif pergunta3 == 'F':
        print('Errou !')
    else:
        print('Resposta Invalida')