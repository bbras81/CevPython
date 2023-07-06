preço = float(input('Qual é o preço do produto? €'))
desc = preço * 5 / 100
print('O produto que custava {}€, na promoção com desconto de 5% vai custar {}€'.format(preço, preço - desc))
