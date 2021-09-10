pessoa = {}
pessoas = []
opção = ""
média = idade = 0
while True:
    pessoa['nome'] = str(input('Nome: ')).strip()
    pessoa['idade'] = int(input('Idade: '))
    pessoa['sexo'] = str(input('Sexo: [F/M] ')).strip().upper()[0]
    pessoas.append(pessoa.copy())
    pessoa.clear()
    opção = str(input('Quer continuar: [S/N]')).strip().upper()[0]
    if 'N' in opção:
        break
for c in range(0, len(pessoas)):
    média += pessoas[c]['idade']
med = média/len(pessoas)
print(f'Ao todo foram cadastradas {len(pessoas)} pessoas')
print(f'A média da idade do grupo é {med}.')
print(f'As mulheres da lista são: ',end='')
for c in range(0, len(pessoas)):
    if pessoas[c]['sexo'] in 'fF':
        print(pessoas[c]['nome'],end=' ')
print()
print(f'As pessoas com idade acima da média são: ',end='')
for c in range(0, len(pessoas)):
    if pessoas[c]['idade'] > med:
        print(pessoas[c]['nome'], end=' ')
print()