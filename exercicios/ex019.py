import random
alu1 = str(input('Digite o nome do 1º Aluno: '))
alu2 = str(input('Digite o nome do 2º Aluno: '))
alu3 = str(input('Digite o nome do 3º Aluno: '))
alu4 = str(input('Digite o nome do 4º Aluno: '))
lista = [alu1, alu2, alu3, alu4]
sort = random.choice(lista)
print('O Aluno escolhido foi o {}'.format(sort))
