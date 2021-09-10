from math import factorial
fat = int(input('Digite um numéro para calcular seu fatorial: '))
cal = fat
print('O fatorial de {} é\n{}! = '.format(fat, fat),end='')
while cal > 0:
    print(cal,end='')
    print(' x ' if cal > 1 else ' = ', end='')
    cal -=1
print(factorial(fat))