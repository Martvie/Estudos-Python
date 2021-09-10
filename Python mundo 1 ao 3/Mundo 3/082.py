list = []
pares = []
impares = []
while True:
    list.append(int(input('Digite um valor: ')))
    opção = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    print(opção)
    if opção in 'Nn':
        break
for c in sorted(list):
    if c % 2 == 0:
        pares.append(c)
    else:
        impares.append(c)
print(f'''A lista completa é {list}
O valores impares são {impares}
Os valores pares são {pares}''')