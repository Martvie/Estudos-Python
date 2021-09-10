maior = 0
menor = 0
for c in range(1, 5):
    peso = float(input('Digite o peso da {} pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('O maior valor foi {}Kg e o menor valor foi {}Kg'.format(maior, menor))