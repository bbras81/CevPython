num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis','sete','oito','nove','dez', 'onze', 'doze', 'treze', 'catorze','quinze','desaseis', 'desassete', 'dezoito', 'desanove','vinte')

while True:
    inNum = int(input('Digite um número entre 0 e 20 '))
    if inNum >= 0 and inNum <= 20:
        print(f'Você digitou o numero {num[inNum]}.')
        break
    else:
        print('Tente novamente. ', end='')
        pass