sal = float(input('Qual o seu salário: '))
if sal <= 1250:
    aumento = (sal/100*15)
else:
    aumento = (sal/100*10)
print('Considerando seu salário de R${:.2f}'.format(sal))
print('Seu aumento será de R${:.2f} totalizando um salário de R${:.2f}'.format(aumento, aumento + sal))