num = int(input('Digite um número: '))
contdiv = 0
for c in range(1, num +1):
    if num % c == 0:
        print('\033[4;32m', end='')
        contdiv += 1
    else:
        print('\033[m', end='')
    print(c,end=' ')
print('\n\033[mO número {} foi divisivel {} vezes.'.format(num, contdiv))
if contdiv == 2:
    print('Logo o número {} é Primo.'.format(num))
else:
    print('Logo o número {} não é primo.'.format(num))