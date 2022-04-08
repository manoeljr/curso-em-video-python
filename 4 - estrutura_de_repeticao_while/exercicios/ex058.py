"""
    Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número
    entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
    mostrando no final quantos palpites foram necessários para vencer.
"""
from random import randint
from time import sleep

opcao = True
cont = 0

while(opcao):
    numero = int(input('Eu pensei em um número de 0 a 10. Qual foi o número que pensei ?'))

    numero_computador = randint(0, 10)
    print('Processando...')
    sleep(2)
    cont += 1

    if numero == numero_computador:
        opcao = False
        break
    else:
        continue

print(f'Foram {cont} tentativas para conseguir acerta a opção')
