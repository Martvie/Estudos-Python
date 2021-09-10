a = int(input('Digite o valor de um lado: '))
b = int(input('Digite o valor de um lado: '))
c = int(input('Digite o valor de um lado: '))
if a < b + c and b < a + c and c < a + b:
    print('Os lados formam um triângulo.')
else:
    print('Os valores não formam um triângulo.')