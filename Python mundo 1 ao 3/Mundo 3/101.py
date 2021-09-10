def voto(num):
    from datetime import date
    ano = date.today().year - num
    if ano < 16:
        return f'Com {ano} anos Você ainda não pode votar'
    elif 16 <= ano < 18 or ano > 65:
        return f'Com {ano} anos seu voto é opicional'
    else:
        return f'Com {ano} anos seu voto é obrigatório!'


print(voto(2000))