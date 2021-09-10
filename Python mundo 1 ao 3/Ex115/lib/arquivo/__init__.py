from lib.interface import *

def arquivoExist(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except (FileNotFoundError):
        return False
    else:
        return True


def arquivoCriar(nome):
    try:
        a = open(nome,'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo.')
    else:
        print('Arquivo criado com Sucesso')


def lerArquivo(nome):
    try:
        a = open(nome,'r')
    except:
        print('ERRO AO LER O ARQUIVO')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(aqu, nome = 'desconhecido', idade = 0):
    try:
        a = open(aqu, 'at')
    except:
        print('Houve um erro na abertura do arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Erro ao inserir dados')
        else:
            print(f'Novo registro de {nome} adicionado')
            a.close()