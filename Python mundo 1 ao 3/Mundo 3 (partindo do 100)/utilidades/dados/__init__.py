def leiadinheiro(msg):
    while True:
        num = str(input(msg)).replace(",", ".").strip()
        if num.isalpha() or num == '':
            print(f'O valor \"{num}\" não é válido')
        else:
            num = float(num)
            break
    return num