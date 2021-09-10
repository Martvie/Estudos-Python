from math import cos, sin, tan, radians

n = int(input('Dite um ângulo '))
n1 = radians(n)
se = sin(n1)
co = cos(n1)
ta = tan(n1)
print('Para o valor de {} você terá:\nSeno igual a {:.2f}\nCosseno igual a {:.2f}\nTangente igual a {:.2f}'.format(n, se, co, ta))
