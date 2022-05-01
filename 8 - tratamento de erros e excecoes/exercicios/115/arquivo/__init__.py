
def arquivo_existe(arquivo):
    try:
        abrir = open(arquivo, 'rt')
        abrir.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(arquivo):
    try:
        arquivo = open(arquivo, 'wt+')
        arquivo.close()
    except:
        print('Houve um ERRO na criação do arquivo')
    else:
        print(f'Arquivo {arquivo} criado com sucesso')


def ler_arquivo(arquivo):
    try:
        a = open(arquivo, 'rt')
    except:
        print('Erro ao ler o arquivo !')
    else:
        print(a.read())
    finally:
        a.close()


def cadastra_pessoa(arquivo, nome='desconhecido', idade=0):
    try:
        a = open(arquivo, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo')
    else:
        try:
            a.write(f'{nome}:{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados')
        else:
            print(f'Novo registro de {nome} adicionado')
            a.close()
