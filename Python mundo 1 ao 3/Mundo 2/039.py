from datetime import date
ano = int(date.today().year)
data = int(input('Qual a sua data de nascimento? '))
if ano - data == 18:
    print('Está na hora de se alistar, se dirija ao posto mais próximo.')
elif ano - data < 18:
    print('Ainda não está na hora de se alistar, você deverá se alistar no ano de {}.'.format((18 - (ano - data)) + ano))
else:
    print('Você ja passou da idade de alistamento, apresente-se o quanto antes.')