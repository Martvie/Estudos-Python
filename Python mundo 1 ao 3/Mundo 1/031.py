km = float(input('Digite a distancia de sua viagem: '))
print('Você está prestes a fazer uma viagem de Km{}.'.format(km))
if km <= 200:
    print('O valor de sua viagem será R${:.2f}'.format(km * 0.5))
else:
    print('O valor de sua viagem será R${:.2f}'.format( km * 0.45))