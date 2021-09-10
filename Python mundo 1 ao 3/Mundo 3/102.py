def fatorial(num=0, show=False):
    """

    :param num: É inserido o número onde calcula-se o fatorial
    :param show: Variavel opicional, se True mostrará o calculo do fatorial
    :return: O fatorial
    """

    f = 1
    for c in range(num, 0, -1):
        if show:
            print(f'{c}',end='')
            if c>1:
                print(f' x ',end='')
            else:
                print(f' = ',end='')
        f *= c
    return f


print(fatorial(3))