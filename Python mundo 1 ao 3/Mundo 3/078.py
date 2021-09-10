lis = []
for c in range(0, 5):
    lis.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        menor = maior = lis[c]
        maior = c
    else:
        if menor > lis[c]:
            menor = lis[c]
        if maior < lis[c]:
            maior = lis[c]
print(f'Você digitou os valores {lis}')
print(f'O menor valor foi o {menor} nas posições ', end=' ')
for p, n in enumerate(lis):
    if n == menor:
        print(f'{p}...',end=' ')
print(f'\nO maior valor foi o {maior} nas posições ', end=' ')
for p, n in enumerate(lis):
    if n == maior:
        print(f'{p}...',end=' ')
