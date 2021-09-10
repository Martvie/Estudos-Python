list = []
for c in range(0, 5):
    num = int(input('Digite um número:'))
    if c == 0 or num > list[-1]:
        list.append(num)
        print(f'O valor {num} foi inserido ao final da lista na posição {len(list)-1} ')
    else:
        pos = 0
        while pos <= len(list):
            if num <= list[pos]:
                list.insert(pos, num)
                print(f'O valor {num} foi inserido na lista na posição {pos}')
                break
            pos += 1
print(list)