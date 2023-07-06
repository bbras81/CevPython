n1 = float(input('Digite a 1ª nota: '))
n2 = float(input('Digite a 2ª nota: '))
média = (n1 + n2) / 2
if média >= 13:
    print('Parabens a sua média é de {} você é um bom aluno'.format(média))
else:
    print('A sua média é de {}, precisa melhorar'.format(média))
