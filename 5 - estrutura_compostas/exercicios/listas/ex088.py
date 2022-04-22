"""
    Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
    O Programa vai perguntar quantos jogos serão gerados e vai sortear
    6 números entre 1 e 60 para cada jogo, cadastrado tudo em uma lista
    composta.
"""

from random import randint
from time import sleep

lista = []
jogos = []
total = 1

print('-' * 30)
print('     Joga na Mega Sena     ')
print('-' * 30)

quantidade_de_jogos = int(input('Quantos jogos você quer que eu sorteie ? '))

while total <= quantidade_de_jogos:
    cont = 0
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
            cont += 1
        if cont >= 6:
            break

    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1

print('=' * 3, f'Sorteando {quantidade_de_jogos} Jogos ', '=' * 3)
for i, linha in enumerate(jogos):
    print(f'Jogo {i + 1}: {linha}')
    sleep(1)
print('Fim do sorteio de jogos')