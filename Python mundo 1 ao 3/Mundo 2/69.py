a = b = c = idade =  0
opção = ' '
while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()
    if idade >= 18:
        a +=1
    elif 'M' in sexo:
        b += 1
    if 'F' in sexo and idade < 20:
        c +=1
    opção = str(input('Deseja encerrar [S/N]: ')).upper().split()
    if 'S' in opção:
        break
    sexo = ' '
print(f'''Dos dados coletados temos o seguinte:
{a} tem 18 anos ou mais
{b} são homens
{c} são mulheres com menos de 20 anos''')