from random import randint
sucessos = jogador = computador = 0
opção = ' '
print('Vamos jogar par ou impar!')
while True:
    print('-='*20)
    jogador = int(input('Digite um número: '))
    while opção not in 'PI':
        opção = str(input('Par ou Impar [P/I]:' )).upper().strip()[0]
    computador = randint(1, 10)
    if 'P' in opção and (jogador + computador) % 2 ==0:
        print('Parabéns, você venceu! Vamos jogar de novo.')
        sucessos +=1
    elif 'I' in opção and (jogador + computador) % 2 !=0:
        print('Parabéns, você venceu! Vamos jogar de novo.')
        sucessos += 1
    else:
        break
print(f'Sinto muito, você perdeu, seu total de vitóroias foram {sucessos}')