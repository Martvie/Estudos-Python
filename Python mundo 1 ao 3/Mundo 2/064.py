para = False
soma = 0
divisor =1
while not para:
    num = int(input('Digite um número [DIGITE 999 PARA PARAR: '))
    if num != 999:
        soma += num
        divisor += 1
    else:
        para = True
divisor = divisor -1
print('''A soma dos valores é {} e foram fornecidos  {} valores.
A média destes é {}'''.format(soma, divisor, soma / divisor))