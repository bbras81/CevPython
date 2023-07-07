from random import randint
numbers = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
#contMaior = numbers[0]
#contMenor = numbers[0]

for number in numbers:
    print(f'{number} ', end='')
print()

#for number in numbers:
#    if number > contMaior:
#        contMaior = number
#    else:
#        pass
    
    
#for number in numbers:
#    if number < contMenor:
#        contMenor = number
#    else:
#        pass
 
numbersS = sorted(numbers)
    
print(f'O numero maior é {numbersS[-1]}')
print(f'O numero menor é {numbers[0]}')
    
    