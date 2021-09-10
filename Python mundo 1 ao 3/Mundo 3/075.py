num = (int(input('Digite um número: ')), int(input('Digite um número: ')),
       int(input('Digite um número: ')), int(input('Digite um número: ')))
print(f'Nos números temos {num.count(9)} noves')
if 3 in num:
    print(f'O primeiro número 3 apareceu na {num.index(3)+1}ª posição')
else:
    print('O número 3 não apareceu na tupla')
print('Os números pares são:',end='')
for c in num:
    if c % 2 == 0:
        print(c, end=' ')