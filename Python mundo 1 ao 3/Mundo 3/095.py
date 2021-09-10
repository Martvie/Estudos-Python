jogador = {}
partidas = []
time = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols na partida{c+1}: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar: [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('Responda corretamente.')
    if resp == 'N':
        break
print('-='*20)
print('cod',end='')
for c in jogador.keys():
    print(f'{c:<15}',end='')
print()
for k, v in enumerate(time):
    print(f'{k:>1}',end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-='*20)
while True:
    busca = int(input('Mostrar dados de qual jogador [999]: '))
    if busca == 999:
        break
    if busca >= len(time):
        print('ERRO, indice não consta no time')
    else:
        print(f'Levantamento do jogador {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'No jogo {i+1} fez {g} gols')
    print('--'*20)