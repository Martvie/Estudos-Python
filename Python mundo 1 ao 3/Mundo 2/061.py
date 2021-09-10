num = int(input('Digire o primeiro termo: '))
raz = int(input('Digite a razão: '))
termos = 1
while termos <= 10:
    print(num, end='')
    print('→' ,end='')
    termos += 1
    num += raz
print('FIM')