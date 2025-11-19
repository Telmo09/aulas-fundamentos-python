# Crie um programa que leia 5 notas de um aluno e calcule a sua média.
#
# >=9.5 passou
# >8 e < 9.5 em recuperação
# <8 reprova

nota1 = float(input('Digite nota 1 : '))
nota2 = float(input('Digite nota 2 : '))
nota3 = float(input('Digite nota 3 : '))
nota4 = float(input('Digite nota 4 : '))
nota5 = float(input('Digite nota 5 : '))

media_nota = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

print(f'Sua média é de {media_nota}')

if media_nota < 8:
    print('Reprovou !')
elif media_nota >= 8 and media_nota < 9.5:
    print('Vais a recuperação')
elif media_nota >= 9.5:
    print('Passaste !')
