list = []
while True:
    num = int(input('Digite um valor: '))
    if num in list:
        print('Valor duplicado, não irei adicionar.')
    else:
        list.append(num)
        print('Valor adicionado com sucesso: ')
    opção = str(input('Deseja continua [s/n]: ')).strip().lower()
    if opção in 'n':
        break
print('-='*20)
list.sort()
print(f'Você digitou os valores{list}')