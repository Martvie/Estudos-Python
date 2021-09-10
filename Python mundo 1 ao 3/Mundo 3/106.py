c = ('\033[0;30;40n',
     '\033[0;30;41m',
     '\033[0;30;42m',
     '\033[0;30;43m',
     '\033[0;30;44m',
     '\033[0;30;45m',
     '\033[0;30;46m')

def ajuda(comando):
    from time import sleep
    sleep(1)
    titulo(f'Acessando dados do comando \'{comando}\'', 4)
    print(c[6],end='')
    sleep(2)
    help(comando)
    print(c[0], end='')


def titulo(msg, cor=0):
    tam = len(msg)
    print(c[cor],end='')
    print(f'~'*tam)
    print(f' {msg}')
    print(f'~' * tam)
    print(c[0],end='')
    print()

comando = ''
while True:
    titulo('Sistema de ajusa Pyhelp', 2)
    comando = str(input('Digite uma função ou biblioteca: '))
    if comando.upper() == 'FIM':
        titulo('Até Logo', 1)
        break
    else:
        ajuda(comando)