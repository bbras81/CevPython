def soma(*valores):
    sum = 0
    for val in valores:
        sum += val
    print(sum)


soma(5, 2)
soma(2, 9, 4)