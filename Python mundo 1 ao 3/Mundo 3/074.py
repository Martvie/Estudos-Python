from random import randint
números = (randint(0, 999), randint(0, 999), randint(0, 999), randint(0, 999), randint(0, 999))
#maior = números[0]
#menor = números [0]
#for c in números:
#    if maior < c:
#        maior = c
#    elif menor > c:
#        menor = c
print(f'''Os valores sorteados foram: {números}
O menor valor foi {min(números)} e o maior foi {max(números)}.''')