n = 0
t = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        n = n + c
        t = t + 1
print('A soma de todos os {} números é {}'.format(t, n))