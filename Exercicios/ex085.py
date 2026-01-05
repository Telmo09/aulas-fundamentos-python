from urllib import request

site = 'https://iefp.pt'
try:
    codigo = request.urlopen(site).getcode()
except:
    print('Erro ao abrir o site')

else:
    print(f'Conseguiu aceder ao site com o codigo {codigo}')