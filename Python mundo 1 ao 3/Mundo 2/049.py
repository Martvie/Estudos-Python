multiplicador = int(input('Qual a tabuada que você quer fazer? '))
for c in range(1, 11):
    print('{} X {} = {}'.format(c, multiplicador, (c * multiplicador)))
print('Fim da tabuada.')