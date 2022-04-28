"""
    Faça um programa que tenha uma função chamada contador(),
    que receba três parâmetros: Inicio, fim e passo e realize
    a contagem. Seu programa tem que realizar três contagens
    através da função criado:
     a) De 1 até 10, de 1 em 1
     b) De 10 até 0, de 2 em 2
     c) Uma contagem personalizada.
"""
from time import sleep


def linha_com_20():
    print('-=' * 20)


def contador(inicio, fim, passo):

    if passo < 0:
        passo *= 1
    if passo == 0:
        passo = 1

    linha_com_20()
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')

    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(2.5)
            cont += passo
        print('FIM !')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= passo
        print('FIM !')


contador(1, 10, 1)
contador(10, 0, 2)
linha_com_20()
print('Agora é a sua vez de personalizar a contagem !')
ini = int(input('Inicio: '))
final = int(input('Final: '))
pas = int(input('Passo: '))

contador(ini, final, pas)
