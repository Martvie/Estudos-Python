n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
    opção = int(input('Sua opção: '))
    if opção == 1:
        print('{} {} {} = {}'.format(n1, '+', n2, n1 + n2))
    elif opção == 2:
        print('{} {} {} = {}'.format(n1, 'X', n2, n1 * n2))
    elif opção == 3:
        if n1 < n2:
            print('O número {} é maior que {}'.format(n1, n2))
        elif n1 == n2:
            print('Os número tem o mesmo valor!')
        else:
            print('O número {} é maior que {}'.format(n1, n2))
    elif opção == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
print('Fim do programa!')