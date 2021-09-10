km = int(input('Qual a velocidade so seu carro? '))
if km > 80:
    print('Você Ultrapassou o limite de velocidade')
    multa = (km - 80) * 7
    print('Você deverá pagar uma multa de R${}'.format(multa))
print('Tenha um bom dia e dirija com segurança.')