list = []
while True:
    list.append(int(input('Digite um valor: ')))
    opção = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    print(opção)
    if opção in 'Nn':
        break
list.sort(reverse=True)
print(f'''A lista tem {len(list)} itens.
A lista decrescente é: {list}''')
if 5 in list:
    print('O número 5 esta na lista', end=' ')
    for p, n in enumerate(list):
         if n == 5:
            print(f'{p}..', end=' ')
else:
    print('O número 5 não esta na lista.')