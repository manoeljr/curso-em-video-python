"""
    Faça um programa que tenha uma função chamada ficha(), que receba dois
    parâmetros opcionais: O nome de um jogador e quantos gols ele marcou.
    O programa deverá ser capaz de mostrar a ficha do jagador, mesmo que
    algum dado não tenha sido informado corretamente.
"""


def ficha(jogador='<desconhecido>', gol=0):
    print(f'O Jogador {jogador} fez {gol} gol(s) no campeonato.')


numero = str(input('Nome do jogador: '))
gol = str(input('Número de gols: '))

if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0


if numero.strip() == '':
    ficha(gol=gol)
else:
    ficha(numero, gol)
