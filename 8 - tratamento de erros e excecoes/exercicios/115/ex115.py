"""
    Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu
    nome e idade em um arquivo de texto simples. O Sistema só vai ter 2 opções:
     - Cadastrar uma nova pessoa e listar todas as pessoas cadastradas.
"""
from interface import cabecalho, menu
from time import sleep


while True:
    resposta = menu(['Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])

    if resposta == 1:
        cabecalho('Opção 1')
    elif resposta == 2:
        cabecalho('Opção 2')
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo !')
        break
    else:
        print('\033[31m[mERRO ! Digite uma opção válida !\033[m')
    sleep(2)
