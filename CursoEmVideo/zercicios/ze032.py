from datetime import date
ano = int(input('Entre com um ano qualquer no formato (YYYY) ou 0 para o ano atual: '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0:
    if ano % 100 != 0:
        print('Ano bissexto')
    else:
        if ano % 400 == 0:
            print('Ano {} bissexto'.format(ano))
else:
    print('Ano {} não é bissexto'.format(ano))