alunos = []
temp = []
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Nota 1: ')))
    temp.append(float(input('Nota 2: ')))
    temp.append(float((temp[1]+temp[2])/2))
    alunos.append(temp[:])
    temp.clear()
    opção = str(input('Deseja continuar [S/N]: '))
    if opção in 'Nn':
        break
print('-='*20)
print(f'{"N°":<4}{"Aluno":<10}{"Média":>8}')
print('-='*20)
for i, a in enumerate(alunos):
    print(f'{i:<4}{a[0]:<10}{a[3]:>8.1f}')
while True:
    opção = int(input('Mostrar notas de qual aluno [999 para]: '))
    if opção == 999:
        break
    else:
        print(f'As notas do {alunos[opção][0]} são {alunos[opção][1]} e {alunos[opção][2]}')
print('Finalizando, volte novamente.')