from datetime import date
trabalhador = {}
trabalhador['Nome'] = str(input('Digite o nome: '))
trabalhador['idade'] = date.today().year - int(input('Digite o ano do seu nascimento: '))
carteira = int(input('Digite o número da sua CTPS [0 se não tiver]: '))
if carteira != 0:
    trabalhador['CTPS'] = carteira
    trabalhador['ano entrada'] = int(input('Ano da sua contratação: '))
    trabalhador['salário'] = float(input('Salário: '))
    trabalhador['Aposentadoria'] = (35 - (date.today().year - trabalhador['ano entrada'])) + trabalhador['idade']
else:
    trabalhador['CTPS'] = 'Não Consta'
print('-='*30)
for k, v in trabalhador.items():
    print(f'{k} tem valor {v}')