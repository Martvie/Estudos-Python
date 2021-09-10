nome = ('zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
        'Quatorze', 'Quinze', 'Dezesseis', 'Desessete', 'Dezoito', 'Dezenove', 'Vinte')
num = int(input('Digite um número entre 0 e 20: '))
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
print(f'Você digitou o número {nome[num]}')
