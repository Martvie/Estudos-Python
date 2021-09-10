from lib.arquivo import *
from time import sleep

arq ='cursoemvideo.txt'

if not arquivoExist(arq):
    arquivoCriar(arq)

while True:
    esc = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do programa'])
    if esc == 1:
        cabeçalho('PESSOAS CADASTRADAS')
        sleep(2)
        #listar o que está no arquivo
        lerArquivo(arq)
        sleep(3)
    elif esc == 2:
        cabeçalho('Opção 2')
        #novo cadastro
        cabeçalho('NOVO CADASTRO')
        sleep(1)
        nome = str(input('Digite o nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif esc == 3:
        cabeçalho('Saindo so sistema... Até logo:')
        break
    else:
        print('\33[31mErro, Digite uma opção válida\33[m')
        sleep(1)