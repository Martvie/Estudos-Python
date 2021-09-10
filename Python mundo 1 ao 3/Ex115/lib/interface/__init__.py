def linha(tam=42):
    print('-' * tam)


def cabeçalho(txt):
    linha()
    print(txt.center(42))
    linha()


def menu(lis):
    cabeçalho('\33[36mMENU PRINCIPAL\33[m')
    c = 1
    for item in lis:
        print(f'\33[32m{c} \33[m- \33[34m{item}\33[m')
        c += 1
    linha()
    opc = leiaint('\33[36mDigite sua opção: \33[m')
    return opc


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
            return num
            break

