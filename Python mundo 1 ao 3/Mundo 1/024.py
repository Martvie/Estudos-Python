#Programa identifica se a cidade começa com santo
cidade = str(input('Em que cidade você nasceu: ')).strip().lower().split()
print('santo' in cidade[0])
cid = str(input('Digite o nome de sua cidade: ')).strip()
print(cid[:5].lower() == 'santo')
