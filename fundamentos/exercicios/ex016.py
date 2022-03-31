"""
    Crie um programa que leia um número real qualquer pelo
    teclado e mostre na tela a seua porção inteira
    Ex.: Digite um número: 6.127
         O Número 6.127 tem a parte inteira 6.
"""

from math import trunc

numero = float(input('Digite um número real : '))

print(f'O Número {numero} tem a parte inteira {trunc(numero)}.')

