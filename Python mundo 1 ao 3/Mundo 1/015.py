d = int(input('Por quantos dias o carro foi alugado? '))
k = float(input('É quantos quilometros foram percorridos? '))
t = (60 * d)+(k * 0.15)
print('O valor a pagar de aluguel será de R${:.2f}.'.format(t))