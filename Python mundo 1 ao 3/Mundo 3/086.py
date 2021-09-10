matriz = [[],[],[]]
for c in range(0,3):
    for d in range(0, 3):
        matriz[c].append(int(input(f'Digite um número para a posição [{c},{d}]: ')))
for c in range (0, 3):
    print(matriz[c])