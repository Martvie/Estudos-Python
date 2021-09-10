media = 0
homemmaisvelho = 0
nomevelho = ''
menos20 = 0
for c in range(1, 5):
    print('----{}°Pessoa----'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo F ou M: ')).lower()
    media += idade
    if c ==1 and sexo =='m':
        homemmaisvelho = idade
        nomevelho= nome
    if sexo == 'm' and idade > homemmaisvelho:
        homemmaisvelho = idade
        nomevelho = nome
    elif sexo == 'f' and idade < 20:
        menos20 += 1
mediaidade = media/4
print('Com os dados coletados temos o seguinte:')
print('''O homem mais velho é o {}.
A média das idades fornecidas é {}.
O total de mulheres com menos de 20 anos é {}.'''.format(nomevelho, mediaidade, menos20))