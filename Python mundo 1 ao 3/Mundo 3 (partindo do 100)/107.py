from utilidades import moeda
p = float(input('Digite um preço: '))
print(f'a metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Acrescido 10%, temos {moeda.aumentar(p, 10)}')
print(f'Reduzido 13%, temos {moeda.diminuir(p, 13)}')