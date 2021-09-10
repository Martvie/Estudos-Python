para = False
acumulador = divisor = média = 0
while not para:
    num = int(input('Digite um número: '))
    acumulador += num
    divisor += 1
    if divisor == 1:
        menor = maior = num
    if menor>num:
        menor = num
    if maior < num:
        maior = num
    resp = str(input('Deseja parar [S/N]: ')).upper().strip()
    if resp == 'S':
        para = True
média = acumulador / divisor
print('''Você digitou {} números, sua soma é {}
E a média destes é {:.2f}
Ainda olhandos seus valores, o menor número foi {} e o maior {}'''.format(divisor, acumulador, média, menor, maior))