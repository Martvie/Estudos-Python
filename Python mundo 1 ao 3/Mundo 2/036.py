valor = float(input('Qual o valor da casa: '))
salário = float(input('Qual o valor do seu salário: '))
tempo = 12 * int(input('Em quantos anos você pretende pagar a casa?'))
prestação = valor / tempo
if prestação <= (salário / 100 * 30):
    print('Emprestimo aprovado!')
elif prestação > (salário / 100 * 30):
    print('Emprestimo Negado')