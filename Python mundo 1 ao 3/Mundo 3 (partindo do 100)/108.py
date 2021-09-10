from utilidades import moeda
p = float(input('Digite um preço: '))
print(f'a metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Acrescido 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Reduzido 13%, temos {moeda.moeda(moeda.diminuir(p, 13))}')