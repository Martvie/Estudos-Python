numero = 0
cont = 0
for n in range(1, 7):
    num = (int(input('Digite o {}° Valor: '.format(n))))
    cont += 1
    if num % 2 == 0:
        numero += num
print('A soma de todos os {} numeros, considerando apenas os pares é {}'.format(cont, numero))