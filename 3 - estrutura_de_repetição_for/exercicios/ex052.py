"""
    Faça um programa que leia um número inteiro e diga se ele é
    ou não um número primo.
"""

numero = int(input('Digite um número : '))

if numero % 1 == 0 and numero % numero:
    print(f'{numero} é número primo')
else:
    print(f'{numero} não é número primo')
