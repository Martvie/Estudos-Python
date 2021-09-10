expr = str(input('Digite a expressão : '))
lista = []
for l in expr:
    if l == '(':
        lista.append(l)
    elif l == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão é válida')
else:
    print('Sua expressão é INVÁLIDA')