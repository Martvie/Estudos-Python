print('{:=^35}'.format('FUKUS REDES'))
preço = float(input('Qual o valor das suas compras: '))
print('''Qual o modo de pagamento?
[1] A vista
[2] A vista no cartão
[3] parcelado em duas vezes no cartão
[4] parcelado em mais vezes no cartão''')
opção = int(input('Sua escolha: '))
if opção == 1:
    print('Sua compra de R${} passará a custar R${}'.format(preço, preço - (preço / 100 * 10)))
elif opção == 2:
    print('Sua compra de R${} passará a custar R${}'.format(preço, preço - (preço / 100 * 5)))
elif opção == 3:
    print('Sua compra irá custar {}'.format(preço))
elif opção == 4:
    prestações = int(input('Em quantas vezes você deseja pagar? '))
    juros = preço/100*20
    print('''Pagando em {} vezes, sua compra terá R${:.2F} de juros, totalizando R${}
O valor de cada parcela será de {}'''.format(prestações, juros, preço + juros, (preço + juros) / prestações))