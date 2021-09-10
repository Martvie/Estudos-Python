from datetime import date
jovem = 0
velho = 0
ano = date.today().year
for c in range(1,8):
    pessoa = int(input('Digite a data de nascimeto da {}° Pessoa: '.format(c)))
    if ano - pessoa > 18:
        velho+=1
    else:
        jovem+=1
print('Tivemos um total de {} pessoas maiores de idade e {} menores'.format(velho, jovem))