from datetime import date
ano = int(date.today().year)
nas = int(input('Qual o ano do seu nascimento? '))
idade = ano - nas
if idade <= 9:
    classe = 'Mirim'
elif idade <= 14:
    classe = 'Infantil'
elif idade <= 19:
    classe = 'Junior'
elif idade <= 20:
    classe = 'Senior'
else:
    classe = 'Master'
print('Olá, sua classe é {}'.format(classe))