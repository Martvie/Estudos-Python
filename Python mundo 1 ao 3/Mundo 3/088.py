from random import randint
from time import sleep
cont = 0
list = []
jogos = []
print('-='*30)
print('JOGOS PARA MEGA')
print('-='*30)
quant = int(input('Quanstos jogos quer que eu sorteie: '))
tot = 0
while tot <= quant-1:
    while True:
        num = randint(1, 60)
        if num not in list:
            list.append(num)
            cont += 1
        if cont < 6:
            continue
        break
    list.sort()
    jogos.append(list[:])
    list.clear()
    cont = 0
    tot += 1
for i, l in enumerate(jogos):
    print(f'O jogo {i+1}: {l}')
    sleep(1)
