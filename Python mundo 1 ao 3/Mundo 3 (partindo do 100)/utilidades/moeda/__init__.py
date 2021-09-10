def aumentar(obj, porcen, m=False):
    '''
    -> Retorna o valor inserido com a porcentagem indicada.
    :param obj: Valor desejado
    :param porcen: Porcentagem desejada
    :return: O valor corrigido
    '''
    x = obj + (porcen * obj / 100)
    return x if not m else moeda(x)


def diminuir(obj, porcen, m=False):
    '''
    -> Retorna o valor inserido retirando a porcentagem indicada.
    :param obj: Valor desejado
    :param porcen: Porcentagem desejada
    :return: O valor corrigido
    '''
    x = obj - (porcen * obj / 100)
    return x if not m else moeda(x)


def dobro(x, m=False):
    x = x * 2
    return x if not m else moeda(x)


def metade(x, m=False):
    x = x / 2
    return x if not m else moeda(x)


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')


def resumo(preço=0, taxa1=10, taxa2=5):
    print('-' * 30)
    print('Resumo Valor'.center(30))
    print('-' * 30)
    print(f'Preço analisado \t{moeda(preço)}')
    print(f'Dobro d preço \t\t{dobro(preço, True)}')
    print(f'Metade do preço \t{metade(preço, True)}')
    print(f'{taxa1}% de aumento\t\t{aumentar(preço, taxa1, True)}')
    print(f'{taxa2}% de redução\t\t{diminuir(preço, taxa2, True)}')
    print('-' * 30)


def leiaint(msg):
    while True:
        try:
            num = int(input(msg))
        except Exception:
            print('\33[31mERRO DIGITE UM NÚMERO INTEIRO\33[m')
        except KeyboardInterrupt:
            print('ENTRADA DE DADOS CANCELADA')
            return 0
            break
        else:
            break

    return num


def leiafloat(msg):
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print('\33[31mERRO DIGITE UM NÚMERO REAL\33[m')
            continue
        except (KeyboardInterrupt):
            print('ENTRADA DE DADOS CANCELADA')
            return 0
            break
        else:
            return num

