def aumentar(obj, porcen, m=False):
    '''
    -> Retorna o valor inserido com a porcentagem indicada.
    :param obj: Valor desejado
    :param porcen: Porcentagem desejada
    :return: O valor corrigido
    '''
    x = obj + (porcen*obj/100)
    if m:
        x = x = f'R$ {x:.2f}'
    return x


def diminuir(obj, porcen,  m=False):
    '''
    -> Retorna o valor inserido retirando a porcentagem indicada.
    :param obj: Valor desejado
    :param porcen: Porcentagem desejada
    :return: O valor corrigido
    '''
    x = obj - (porcen*obj/100)
    if m:
        x = f'R$ {x:.2f}'
    return x


def dobro(x,  m=False):
    x = x*2
    if m:
        x = f'R$ {x:.2f}'
    return x


def metade(x, m=False):
    x = x/2
    if m:
        x = f'R$ {x:.2f}'
    return x