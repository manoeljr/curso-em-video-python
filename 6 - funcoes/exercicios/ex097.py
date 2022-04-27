"""
    Faça um programa que tenha uma função  chamada escreva(), que receba
    um texto qualquer como parâmetro e mostre uma mensagem com tamanho
    adaptável.
        Ex.:
            escreva('Olá, Mundo !')
        saida:
            ~~~~~~~~~~~~~~~~~~
                Olá, Mundo !
            ~~~~~~~~~~~~~~~~~~
"""


def escreva(mensagem):
    tamanho_mensagem = len(mensagem) + 4
    print('~' * tamanho_mensagem)
    print(f'    {mensagem}')
    print('~' * tamanho_mensagem)


escreva('Primeiro')
