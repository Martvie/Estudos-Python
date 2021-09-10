num = int(input('Digite um número que será convertido: '))
print('''Suas opções de conversão são as seguintes.
[1] BINÁRIO
[2] OCTAL
[3] HEXADECIMAL''')
opção = int (input('Sua opção: '))
if opção == 1:
    print('O número {} convertido para BINÁRIO é {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('O número {} convertido para OCTAL é {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('O número {} convertido para HEXADECIMAL é {}'.format(num, hex(num)[2:]))
else:
    print('A opção escolhida é inválida.')