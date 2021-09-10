from random import randint
from time import sleep
computador = randint(0, 10)
print('Olá, vamos jogar um jogo? Vou pensar em um número de 0 a 10\nTente adivinhar qual é!')
sleep(1)
print('Vamos lá...')
sleep(3)
acertou = False
tentativa = 1
jogador = int(input('Vamos lá, que número você achaa que é?: '))
while not acertou:
    jogador = int(input('Resposta errada, tente mais uma vez: '))
    tentativa += 1
    if jogador == computador:
        acertou = True
print('Parabens, você acertou, eu pensei no número {}\n Para acertar você levou {} tentativas'.format(computador, tentativa))