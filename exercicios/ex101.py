from datetime import date
def voto(ano):
    anoActual = date.today().year
    idade = anoActual - ano
    if idade >= 18 and idade < 65:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO')
    elif idade > 65:
        print(f'Com {idade} anos: VOTO OPCIONAL')
    else:
        print(f'Com {idade} anos: NÃO VOTA!')

print('-' * 30)
anoNasc = int(input('Em que ano você nasceu? '))
voto(anoNasc)