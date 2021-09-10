from random import randint
from time import sleep

opções = randint(1, 3)
if opções == 1:
    comp = 'pedra'
elif opções == 2:
    comp = 'papel'
elif opções == 3:
    comp = 'tesoura'
print('Vamos jogar jokenpô?')
print('''Escolha sua jogada:
01 pedra
02 papel
03 tesoura''')
escolha = int(input('Sua escolha: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
if escolha > opções:
    print('Parabens, você GANHOU! eu escolhi {}'.format(comp))
elif escolha == opções:
    print('Parece que escolhemos a mesma coisa e deu EMPATE!')
else:
    print('Que pensa, eu escolhi {} e ganhei de você'.format(comp))