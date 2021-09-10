lista = ('Lapís', 1.75,
         'Borracha', 2,
         'caderno', 5)
for pos in range(0, len(lista)):
    if pos % 2 ==0:
        print(f'{lista[pos]:.<10}', end='')
    if pos % 2 == 1:
        print(f'{lista[pos]:.>10}')