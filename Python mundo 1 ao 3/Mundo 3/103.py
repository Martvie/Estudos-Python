def ficha():
    """
    O programa recebe e mostra o nome do jogador e seu total de gols
    :return:
    """
    nome = str(input('Insira o nome do jogador: '))
    if nome =='':
        nome = '<desconhecido>'
    gols = str(input('Quantos gols ele fez: '))
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato')


ficha()