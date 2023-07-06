a = input('Digite algo: ')
# Para usar o comando type, tem que se usar uma virgula a seguir á aspa simples. Depois type e (variável).
print('o tipo primitivo deste valor é: ', type(a))
print('{} Só tem espaços?'.format(a.upper()), a.isspace())
print('{} É um numero? '.format(a), a.isalnum())
print('{} É alfabético? '.format(a), a.isalpha())
print('{} É alfanumérico? '.format(a), a.isalnum())
print('{} Está em maiusculas? '.format(a), a.isupper())
print('{} Está em minusculas? '.format(a), a.islower())
print('{} Está capitalizada? '.format(a), a.istitle())
# Para usar o format /Colocar chaveta no texto e SEM VIRGULA, por o .format (variavel(eis) e o tipo de formatação).
