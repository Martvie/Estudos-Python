n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
if n1>n2 :
    print('O primeiro valor {} é maior que {}'.format(n1, n2))
elif n1<n2:
    print('O segundo valo {} é maior que {}'.format(n2, n1))
else:
    print('Não existe um valor maior, os dois são iguais.')