fra = str(input('Digite uma frase: ')).strip()
convert = fra.lower().replace(' ','')
palin =''
for letra in range (len(convert)-1,-1,-1):
    palin += convert[letra]
if convert == palin:
    print('É um palindromo')
else:
    print('Não é um palindromo.')