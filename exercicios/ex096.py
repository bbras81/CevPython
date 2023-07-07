def area(lar, comp):
    ar = lar * comp
    print(f'A área de um terreno {lar} x {comp} é de {ar}m2.')

def titulo(msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)

titulo('Controle de Terrenos')
lar = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))

area(lar, comp)
