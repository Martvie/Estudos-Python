a = int(input('Digite um número: '))
b = int(input('Digite um número: '))
c = int(input('Digite um número: '))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
maior = b
if a>b and a>c:
    maior = a
if c > b and c > a:
    maior = c
print('Analisando os números {}, {} e {} temos que:'.format(a, b, c))
print('Seu maior valor é {}\nSeu menor valor é {}'.format(maior, menor))