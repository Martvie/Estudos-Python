numeros = input('Digite um número de quatro digitos: ')
print('unidade: {}'.format(numeros[3:]))
print('dezenas: {}'.format(numeros[2:3]))
print('centenas: {}'.format(numeros[1:2]))
print('milhar: {}'.format(numeros[0:1]))
#outra maneira
num = int(input('Digite um numero de 4 digitos: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print("""Analisando o numero {}, temos que:
Unidades: {}\nDezenas: {}\nCentenas: {}\nMilhar: {}""".format(num, u, d, c, m))
#o ultimo código esta mais correto