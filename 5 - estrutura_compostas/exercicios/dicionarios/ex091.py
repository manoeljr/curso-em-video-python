"""
    Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
    Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem
    sabendo que o vencedor tirou o maior número no dado.
"""
from random import randint
from time import sleep
from operator import itemgetter


jogo = {
    'jogador 1': randint(1, 6),
    'jogador 2': randint(1, 6),
    'jogador 3': randint(1, 6),
    'jogador 4': randint(1, 6),
}
ranking = {}

print('Valores sorteados: ')
for key, value in jogo.items():
    print(f'{key} tirou {value} no dado.')
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('== Ranking dos jogadores ==')
for index, value in enumerate(ranking):
    print(f'{index + 1}° lugar: {value[0]} com {value[1]}.')
    sleep(1)

