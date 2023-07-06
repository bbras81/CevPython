from math import hypot
# forma matematica.
cat = float(input('Comprimento do cateto oposto: '))
catad = float(input('Qual o comprimento do cateto adjacente: '))
# hip = (cat**2 + catad**2)**0.5
hip = hypot(cat, catad)
print('A hipotenusa vai medir {:.2f}'.format(hip))
