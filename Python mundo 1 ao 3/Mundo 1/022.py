# Funciona, no começo adicionei o comando strip
nome = str(input('Qual o seu nome: ')).strip()
contagem = len(nome.replace(' ', ''))
primeiro = nome.split()
print("""Olá {}, vamos ver informações do seu nome então
Seu nome em maisculas é {}.
Seu nome em minsculas é {}.""".format(nome, nome.upper(), nome.lower()))
print('Seu nome ao todo contem {} letras.'.format(contagem))
print('E seu primeiro nome é {} e ele tem {} letras'.format(primeiro[0], len(primeiro[0])))
# Versão com menos variaveis
print('----------------------')
print('Olá {} vamos ver algumas informações do seu nome.'.format(nome))
print('Seu nome em maiusculas é {}.'.format(nome.upper()))
print('Seu nome em minusculas é {}.'.format(nome.lower()))
print('Seu nome {}\nContem ao todo {} letras.'.format(nome, len(nome) - nome.count(' ')))
print('Seu primeiro nome é {}, e contem {} letras.'.format(primeiro[0], len(primeiro[0])))
