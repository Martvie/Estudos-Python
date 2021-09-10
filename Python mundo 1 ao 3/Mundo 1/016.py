from math import trunc

num = float(input('Digite um numero real: '))
print('A parte inteira de {} é {}.'.format(num, trunc(num)))
#Outro modo
print('A parte inteira de {} é {}'.format(num, int(num)))
