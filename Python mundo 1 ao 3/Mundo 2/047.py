n = int(0)
for c in range(0,50+1): # posso fazer com (2, 51, 2):
    n = n + 1
    if n % 2 == 0:
        print(n,end=', ')
print('Fim')