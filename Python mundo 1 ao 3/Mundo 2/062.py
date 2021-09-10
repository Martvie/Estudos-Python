num = int(input('Digire o primeiro termo: '))
raz = int(input('Digite a razão: '))
termos = 10
opção = 1
cont = 0
while opção != 0:
    while termos >=0:
        print(num,'→', end='')

        termos -= 1
        num += raz
        cont += 1
    print('Pausa', end='')
    opção = int(input('\nQuanto mais termos você quer ver? '))
    if opção > 0:
        termos += opção
    else:
        opção = 0
print('Fim, foram mostradas {} Termos'.format(cont))