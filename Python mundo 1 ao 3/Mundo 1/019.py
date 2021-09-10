from random import choice

n1 = str(input('Digite o nome de um aluno: '))
n2 = str(input('Digite o nome de um aluno: '))
n3 = str(input('Digite o nome de um aluno: '))
n4 = str(input('Digite o nome de um aluno: '))
lista = [n1, n2, n3, n4]
r = choice(lista)
print('O aluno(a) escolhido foi {}'.format(r))
