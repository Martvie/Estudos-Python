from random import randint
from time import sleep
def sorteio(lista):
    print('Sorteando 5 valores em uma lista ', end='')
    for cont in range(0, 5):
        n = randint(1, 50)
        lista.append(n)
        print(f'{n}', end=' ')
        sleep(.3)
    print()
def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma destes valores é {soma}')


numeros = []
sorteio(numeros)
somapar(numeros)