# Inserir o .strip na declaração do primeiro string elimina logo á partida todos os espaços.
nome = str(input('Digite o seu nome completo: ')).strip()
print('Analizando o seu nome:')
print('O seu nome em MAIUSCULAS É: {}'.format(nome.upper()))
print('O seu nome em minusculas é:{}'.format(nome.lower()))
# Depois no print basta eliminar os espaços no meio do nome (estes nao são eliminados pelos strip)
print('O seu nome tem {} letras.'.format(len(nome) - nome.count(' ')))
'''Aqui contamos o primeiro nome usando o find até ao primeiro espaço,
que indica a quantidades de caracteres usados até ao primeiro espaço'''
print('O seu primeiro nome é {}'.format(nome.find(' ')))
# Outra forma de fazer este ultimo
separa = nome.split()
print('O seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))
