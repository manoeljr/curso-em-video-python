"""
    Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu
    nome e idade em um arquivo de texto simples. O Sistema só vai ter 2 opções:
     - Cadastrar uma nova pessoa e listar todas as pessoas cadastradas.
"""
from interface import cabecalho, menu, leia_int
from arquivo import arquivo_existe, criar_arquivo, ler_arquivo, cadastra_pessoa
from time import sleep

arquivo = 'curso_em_video.txt'

if not arquivo_existe(arquivo):
    criar_arquivo(arquivo)

while True:
    resposta = menu(['Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])

    if resposta == 1:
        ler_arquivo(arquivo)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leia_int('Idade: ')
        cadastra_pessoa(arquivo, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo !')
        break
    else:
        print('\033[31m[mERRO ! Digite uma opção válida !\033[m')
    sleep(2)
