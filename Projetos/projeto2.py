# Desenvolva uma aplicação que faça o :
# registo do username
# email
# e password de um utilizador.
#
# O programa deverá:
# 1- Dar as boas vindas
# 2- Pedir para registar username, email e password
# 3- Exibir uma mensagem de sucesso
# 4- Aparecer um menu com as opções “Login” e “Sair”
# 5- Ao fazer login deve aparecer uma mensagem de boas vindas
# 6- Caso o utilizador erre a password ou username, o sistema
# deve permitir que tente novamente o login e caso erre novamente, o programa deve
# exibir uma mensagem a informar que a conta está bloqueada e terminar.

print('Bem vindo ao interface !')
print('Para iniciar, deve registar a sua conta')
username = input('Qual seu username ? ').strip()

while True:
    mail = input('Associe um email: ').strip()
    mail_ver = mail.find('@')
    mail_p = mail[mail_ver:]

    if '@' in mail and '.' in mail_p:
        break
    else:
        print('Erro no email, tente novamente!')


password = input('Qual sua password ? ').strip()
print('--- REGISTO CRIADO COM SUCESSO ---')

print('Selecione uma opção :')
print('[1] - Login')
print('[2] - Sair')

while True:
    menu = int(input('Digite uma opção : '))

    if menu == 1:
        print('Faça o seu login')
        break
    elif menu == 2:
        print('Saída com sucesso')
        exit()
    else:
        print('Erro: opção inválida, tente novamente.')

login_user = input('Qual seu username ? : ').strip()
login_pw = input('Qual a password ? : ').strip()

if username == login_user and password == login_pw:
    print('Logado com sucesso !')
else:
    print('Login incorreto')
    login_user = input('Qual seu username ? : ').strip()
    login_pw = input('Qual a password ? : ').strip()

    if username == login_user and password == login_pw:
        print('Logado com sucesso !')
    else:
        print('Conta foi bloqueada !')
