a = float(input('Digite o valor '))
b = float(input('Digite o valor '))
c = float(input('Digite o valor '))
if a + b > c and c + b > a and a + c > b:
    print('O trinângulo existe e é ',end = '')
    if a == b == c:
        print('equilátero')
    elif a != b != c !=a:
        print('escaleno')
    else:
        print('isoceles')
else:
    print('O triangulo não existe.')