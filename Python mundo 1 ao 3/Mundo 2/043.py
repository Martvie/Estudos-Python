al = float(input('Qual a sua altura? '))
pe = float(input('Digite seu peso: '))
imc = pe / (al**2)
if imc < 18.5:
    categoria = 'Abaixo do peso'
elif imc >= 18.5 and imc < 25:
    categoria = 'Peso ideal'
elif imc >= 25 and imc < 30:
    categoria = 'Sobrepeso'
elif imc >= 30 and imc < 40:
    categoria = 'obesidade'
else:
    categoria = 'Fodeu tu vai morrer mané'
print('Considerando os valores oferecidos seu imc é {:.2f} identificado como {}'.format(imc, categoria))
