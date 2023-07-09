def mensagem(msg):
    print('-' * 30)
    print(msg.upper())
    print('-' * 30)


def soma(a, b):
    s = a + b
    print(s)


def contador(*num):
    sum = 0
    for v in num:
        sum += v
    print(sum)



'''
mensagem('sistema de alunos')



mensagem('ESTUDONAUTA')
mensagem('APRENDA COM PYTHON')
mensagem('GUSTAVO GUANABARA')


Aqui esta os comentários multi-linha
'''

soma(2, 4)
contador(2, 1, 7)
contador(3, 2, 6, 78, 3)
