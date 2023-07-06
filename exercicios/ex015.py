al = float(input('Quantos dias o carro foi alugado? '))
km = int(input('Quantos quilometros o carro precorreu? '))
# kmr = km * 0.15
# dias = al * 60
pago = (al * 60) + (km * 0.15)
print('O total a pagar é de {:.2f}€'.format(pago))
