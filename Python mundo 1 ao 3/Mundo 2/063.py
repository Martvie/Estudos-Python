seque = int(input('Quantos termos você quer ver da sequencia de Fibonate? '))
num = 0
t1 = 0
t2 = 1
print('{}, {}, '.format(t1, t2), end='')
while seque != 0:
    t3 = t1 + t2
    print(t3,end='')
    print(' ,' if seque > 1 else ' ', end='')
    seque-=1
    t1 = t2
    t2 = t3
print('FIM')