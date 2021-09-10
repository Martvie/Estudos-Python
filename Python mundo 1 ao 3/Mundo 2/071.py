print('='*30)
print('{:^30}'.format('BEM VINDO AO TULIUS BANK'))
print('='*30)
valor = int(input('Quanto você deseja sacar: '))
total = valor
céd = 50
totalcedulas = 0
while True:
    if total>= céd:
        total -= céd
        totalcedulas +=1
    else:
        print(f'Total de {totalcedulas} cédulas de {céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 5
        elif céd == 5:
            céd = 1
        totalcedulas = 0
        if total == 0:
            break