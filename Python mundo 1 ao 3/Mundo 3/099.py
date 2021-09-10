from time import sleep
def maior(*num):
    print('-='*30)
    print('Analisando valores')
    sleep(1)
    cont = maior = 0
    for valor in num:
        print(f'{valor}', end=' ')
        sleep(.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informador {cont} valores ao todo')
    print(f'O maior valor foi {maior}')
maior(1, 5, 8, 9, 4)
