a = b = preço = cont  = 0
c = nome = ' '
cpreço = 0
while True:
    nome = str(input('Digite o produto: '))
    preço = float(input('Digite o preço: '))
    if cont == 0 or preço < cpreço:
        cpreço = preço
        c = nome
    cont +=1
    a += preço
    if preço >= 1000:
        b += 1
    opção = ' '
    while opção not in 'SN':
        opção = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    if 'N' in opção:
        break
print(f'''O total da compra foi R${a}
{b} pordutos custam mais de R$1000
o produto mais barato foi {c}.''')
