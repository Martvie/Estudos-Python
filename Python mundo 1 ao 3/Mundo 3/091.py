from random import randint
from time import sleep
from operator import itemgetter
jogo = {'Jogador1': randint(1, 6),
        'Jogador2': randint(1, 6),
        'Jogador3': randint(1, 6),
        'Jogador4': randint(1, 6)}
ranking = {}
sleep(1)
print('Valores sorteados')
sleep(1)
for k, v in jogo.items():
    print(f'O {k} tirou {v}')
    sleep(1)
print('O ranking é')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i} Lugar {v[0]} {v[1]}')
