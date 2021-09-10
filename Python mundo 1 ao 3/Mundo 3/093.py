rendimento = {}
gols = []
tot = 0
jogos = 1
rendimento['nome'] = str(input('Nome do jogador: '))
partidas = int(input('Quantas partidas ele jogou: '))
rendimento['gols'] = gols
while jogos <= partidas:
    pontos = int(input(f'Quantos gols ele fez na partida {jogos}: '))
    rendimento['gols'].append(pontos)
    jogos += 1
    tot += pontos
rendimento['total'] = tot #depois tentar metodo com sum
print('-=' * 20)
print(rendimento)
print('-=' * 20)
for k, v in rendimento.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 20)
print(f'O jogador {rendimento["nome"]} jogou {len(rendimento["gols"])} jogos.')
for p, g in enumerate(rendimento['gols']):
    print(f'==> Na partida {p} ele fez {g} Gols')
