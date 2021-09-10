from math import hypot

co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente '))
print('Com o cateto oposto {} e o cateto adjacente {}\nSua hipotenusa será {}.'.format(co, ca, hypot(co, ca)))
