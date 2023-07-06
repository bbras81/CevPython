from random import randint
from time import sleep
print('-=-'*20)
print('Vou pensar um número entre 0 e 5. Tente adivinhar!')
print('-=-'*20)
np = int(input('Em que numero pensei? '))
print('PROCESSANDO!!!')
sleep(3) # Faz o programa esperar 3 segundos
n = randint(0, 5)
if np == n:
    print('Parabens você acertou!!!')
else:
    print('Eu ganhei pensei no numero {} e você no {}. Pouca sorte!!!'.format(n, np))
