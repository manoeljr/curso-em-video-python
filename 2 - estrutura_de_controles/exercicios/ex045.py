"""
    Crie um programa que faça o computador jogar JOKENPÔ(pedra, papel e tesoura) com você
"""
from random import randrange

escolha = int(input('Vamos jogar ?\n'
                    'Escolha sua opção :\n'
                    '1 - Pedra\n'
                    '2 - Papel\n'
                    '3 - Tesoura\n'
                    'Faça sua escolha : '))

escolhas = ['pedra', 'papel', 'tesoura']

computador = randrange(escolhas)

print(computador)
