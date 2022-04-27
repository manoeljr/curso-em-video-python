"""
    Faça um programa que tenha uma função chamada área(),
    que receba as dimensões de um terreno retangular
    (largura e comprimento) e mostre a área do terreno.
"""


def area(largura, comprimento):
    print(f'Área de um terreno retangular é {comprimento * largura} metros quadrados.')


largura = float(input('Largura do terreno: '))
comprimento = float(input('Comprimento do terreno: '))

area(largura, comprimento)
