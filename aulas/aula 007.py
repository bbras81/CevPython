tit1 = 'OPERADORES ARITEMÉTICOS'
print('{:-^60}'.format(tit1).upper())
# (+)  adição
a = int(5 + 3)
print(a)
# (-)  subtração
s = int(10-3)
print(s)
# (*)  multiplicação
m = int(3*6)
print(m)
# (/)  divisão
d = int(8 / 6)
print(d)
# (**) potencia
p = int(6**2)
print(p)
# (//) divisão inteira
di = int(5//2)
print(di)
# (%)  resto "modulo"
r = int(26 % 3)
print(r)
tit = 'Ordem dos operadores'
print('{:-^60}'.format(tit).upper())
# 1º () parentesis
par = int(3*(5+4)**2)
print('a ordem do problema (3*(5+4)**2) é ( () ** * e o reultado é 243, confere: {}'.format(par))
# 2º ** Potências
pot = int(3*5+4**2)
print('a ordem do problema (3*5+4**2) é (** * + ) e o resultado é 31 confere: {}'.format(pot))
# 3º * multiplicação / divisão // divisão inteira % modolo
m = int(5+3*2)
print('a ordem do problema (5+3*2) é (* +) resultado 11 confere: {}'.format(m))
# 4º + adição - subtração
