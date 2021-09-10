matriz = [[],[],[]]
somapares = somaterceira = maior = 0
for c in range(0,3):
    for d in range(0, 3):
        matriz[c].append(int(input(f'Digite um número para a posição [{c},{d}]: ')))
print('-='*20)
for l in range (0, 3):
    for c in range (0, 3):
        num = matriz[l][c]
        print(f'[{matriz[l][c]:^3}]',end='')
        if matriz[l][c] % 2 ==0:
            somapares += matriz[l][c]
    print()
print('-='*20)
print(f'A soma dos valores pares digitados é {somapares}')
for l in range(0, 3):
    somaterceira += matriz[l][2]
print(f'A soma dos valores da terceira fileira é {somaterceira}')
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    else:
        if maior < matriz[1][c]:
            maior = matriz[1][c]
print(f'O maior valor da segunda linha é {maior}')