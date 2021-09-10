inicio = int(input('Digite o inicio: '))
razão = int(input('Digite a razão: '))
decimo = inicio + (10 - 1) * razão
for c in range(inicio, decimo, razão):
    print(c, end=', ')
print('Fim.')