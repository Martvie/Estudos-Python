def leiaint():
    while True:
        num = input('Digite um número: ')
        if num.isnumeric():
            num = int(num)
            break
        else:
            print('Erro Digite um número')
            num = input('Digite um número: ')
    print(f'Você digitou o numero {num}')
    return num


n =leiaint()
print(n)