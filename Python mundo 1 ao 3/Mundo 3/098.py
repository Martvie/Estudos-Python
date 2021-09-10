from time import sleep
def contador(i, f, p):
    if p == 0:
        p = 1
    print('-='*20)
    print(f'Contadem de {i} ate {f} de {p} em {p}')
    if i < f:
        cont = i
        while cont < f:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont += p
        print('Fim!')
    else:
        cont = i
        while cont > f:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont -= p
        print('Fim!')

contador(1, 10, 1)
contador(10, 1, 1)
print('Agora é sua vez de fazer a contagem!')
ini = int(input('Digite o início: '))
fim = int(input('Digite o fim: '))
inte = int(input('Digite o intervalo: '))
contador(ini, fim, inte)