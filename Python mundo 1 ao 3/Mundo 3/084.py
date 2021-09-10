pessoas = []
dados = []
maiorp = menorp = 0
while True:
    dados.append(str(input('Nome da pessoa: ')))
    dados.append(float(input('Peso da pessoa: ')))
    if len(pessoas) == 0:
        maiorp = menorp = dados[1]
    else:
        if maiorp < dados[1]:
            maiorp = dados[1]
        elif menorp > dados[1]:
            menorp = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    opção = str(input("Deseja continuar [S/N]: ")).strip().upper()[0]
    if opção in 'Nn':
        break
print(f'Você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi {maiorp}Kg. Peso de ',end='')
for p in pessoas:
    if p[1] == maiorp:
        print(p[0],end=' ')
print(f"\nO menor peso foi {menorp}Kg. Peso de ", end='')
for p in pessoas:
    if p[1] == menorp:
        print(p[0],end=' ')