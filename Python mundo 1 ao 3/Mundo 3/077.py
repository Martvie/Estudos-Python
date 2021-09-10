palavras = ('Aprender', 'Cansado', 'Chega')
for p in palavras:
    print(f'\nA palavra {p} tem as vogais: ',end ='')
    for letras in p:
        if letras.lower() in 'aeiou':
            print(letras, end=' ')