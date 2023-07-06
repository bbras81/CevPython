from datetime import date

ano = int(input('Que ano quer analizar? Coloque 0 para analizar o ano actual:'))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é Bissesto'.format(ano))
else:
    print('O ano {} não é Bissesto'.format(ano))