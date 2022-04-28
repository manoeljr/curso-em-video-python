"""
    Faça um programa que tenha uma função chamada maior(),
    que receba vários parêmetros com valores inteiros.
    Seu programa tem que analisar todos os valores e
    dizer qual deles é o maior.
"""


def maior(* valores):
    if valores:
        print(f'Maior valor {max(valores)}')
    else:
        print('Não existe valor maior')


maior(1, 56, 99)
