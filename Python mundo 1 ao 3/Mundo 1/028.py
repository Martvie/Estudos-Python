from random import randint
from time import sleep
adi = randint(0, 1)
print('Vou pensar em um número, tente adivinhar')
print('Estou pensando....')
sleep(3)
num = int(input('Que numero você acha que eu pensei: '))
if num == adi:
    print('Parabens você acertou!')
else:
    print('Sinto muito, você errou, eu havia pensado no numero {}.'.format(adi))