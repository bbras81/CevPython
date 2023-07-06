n1 = int(input('um valor: '))
n2 = int(input('outro valor: '))
print('A soma vale {}'.format(n1+n2))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
#                               formata as casas decimais / evita a quebra de um print para o outro ')
print('a soma {}, \n o produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' ')
print('divisão inteira {} e potencia {}'.format(di, e))