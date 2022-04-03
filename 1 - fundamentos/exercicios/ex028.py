"""
    Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
    e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
    O Programa deverá escrever na tela se o usuário venceu ou perdeu.
"""

from random import randint
from time import sleep

numero = int(input('Eu pensei em um número de 0 a 5. Qual foi o número que pensei ?'))

numero_computador = randint(0, 5)

print('Processando...')
sleep(2)

if numero == numero_computador:
    print(f'Você acertou o número !\n'
          f'Meu número foi {numero_computador}\n'
          f'O Seu número foi {numero}')
else:
    print(f'Você Errou o número !\n'
          f'Número do computador {numero_computador}\n'
          f'Você digitou {numero}')
