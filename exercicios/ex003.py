# Declaração de tipo de variavél
# nome = tipo ()
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
s = n1 + n2
# Print dos valores com as variaveis colocadas no texto entre virgulas.
print('A soma entre', n1, 'e', n2, 'é de: ', s)
# Para usar o ".format" colocar chavetas no texto e declarar a variavel a seguir ao .format dentro de parentesis.
print('A soma entre {} e {} é de {}... '.format(n1, n2, s))
