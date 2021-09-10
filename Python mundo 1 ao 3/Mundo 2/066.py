num = total = cont = 0
while True:
    num = int(input('Digite um número [Digite 999 para parar: '))
    if num == 999:
        break
    total += num
    cont += 1
print(f'''A soma dos números digitados foi {total}
Você digitou {cont} números''')
