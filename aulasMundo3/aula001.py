#Tuplas são imutáveis

lanche = ('hamburger', 'sumo', 'pizza', 'pudim')
print(lanche[2:])

for c in lanche:
    print(c)
    
for pos, c in enumerate(lanche):
    print(f'eu vou vomer {c} na posição {pos + 1}')
    
    
for cont in range(0, len(lanche)):
    print(lanche[cont])
    
    
print(sorted(lanche))