nr = int(input('Informe um número: '))
u = nr // 1 % 10
d = nr // 10 % 10
c = nr // 100 % 10
m = nr // 1000 % 10
print('Analizando o numero {}:'.format(nr))
print('unidade: {}'.format(u))
print('Dezenas: {}'.format(d))
print('Centenas: {}'.format(c))
print('Milhares: {}'.format(m))
