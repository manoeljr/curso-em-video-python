"""
    Faça um programa que joque par ou impar com o computador.
    O Jogo só será interrompido quando o jogador PERDER, mostrando
    o total de vitórias consecutivas que ele conquistou no final do jogo.
"""
from random import randint
from time import sleep
vitoria = 0

while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '

    while tipo not in 'PI':
        tipo = str(input('Digite [P/I]: ')).strip().upper()[0]

    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}. ', end='')
    print(' Deu PAR' if total % 2 == 0 else 'Deu IMPAR')

    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU !')
            vitoria += 1
        else:
            print('você PERDEU !')
            break
    elif tipo == 'I':
        if total % 2 == 0:
            print('Você VENCEU !')
            vitoria += 1
        else:
            print('você PERDEU !')
            break
    print('Vamos jogar novamente...')
    sleep(2)

print(f'Game Over ! Você venceu {vitoria} vezes.')
