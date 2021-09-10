from random import shuffle
n1 = str(input('Primeiro estudante: '))
n2 = str(input('Segundo estudante: '))
n3 = str(input('Terceiro estudante: '))
n4 = str(input('Quarto estudante: '))
lista = [n1, n2, n3, n4]
escolhido = shuffle(lista)
print('A ordem é: ')
print(lista)