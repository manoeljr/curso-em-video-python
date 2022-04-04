"""
    Crie um programa que faça o computador jogar JOKENPÔ(pedra, papel e tesoura) com você
"""
from random import randint
from time import sleep

print('''Vamos jogar ?
Escolha sua opção :
    [ 1 ] Pedra
    [ 2 ] Papel
    [ 3 ] Tesoura
''')

jogador = int(input('Qual a sua opão : '))

opcoes = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ !!!')
sleep(1)

print('-=' * 11)
print(f'Computador jogou {opcoes[computador]}')
print(f'Jogador jogou {opcoes[jogador]}')
print('-=' * 11)

if computador == 0:
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador vence')
    elif jogador == 2:
        print('Computador vence')
    else:
        print('Jogada Inválida')
elif computador == 1:
    if jogador == 0:
        print('Computador vence')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador vence')
    else:
        print('Jogada Inválida')
elif computador == 2:
    if jogador == 0:
        print('Jogador vence')
    elif jogador == 1:
        print('Computador vence')
    elif jogador == 2:
        print('Empate')
    else:
        print('Jogada Inválida')
else:
    print('Jogada Inválida')
