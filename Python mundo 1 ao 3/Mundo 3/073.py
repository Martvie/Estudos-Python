times = ('Flamengo', 'Internacional', 'Atlético-MG', 'São Paulo', 'Fluminense', 'Gremio',
         'Palmeiras', 'Santos', 'Atlético-PR', 'Bragantino', 'Ceará-SC', 'Corinthians',
        'Atlético-GO', 'Bahia', 'Sport Recife', 'Fortaleza', 'Vasco da Gama', 'Goiás', 'Curitiba', 'Botafogo')
print(f'Os 5 primeiros colocados são {times[0:5]}')
print(f'Os 4 ultimo colocados são {times[-4:]}')
print(f'A ordem alfabética dos times é {sorted(times)}')
time = 'Goiás'
print(f'O time goiás está na posição {times.index(time)}')