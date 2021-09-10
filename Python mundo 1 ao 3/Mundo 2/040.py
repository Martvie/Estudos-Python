m1 = float(input('Qual sua primeira nota? '))
m2 = float(input('Qual sua segunda nota? '))
media = (m1+m2)/2
if media < 5.9:
    print('Sinto muito, você foi reprovado.')
elif media >= 5.9 and media <= 6.9:
    print('Quase ein! Você está de recuperação.')
else:
    print('Parabéns, você foi aprovado!')