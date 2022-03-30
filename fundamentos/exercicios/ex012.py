"""
    Faça um algoritmo que leia o preço de um produto e
    mostre seu novo preço, com 5% de desconto.
"""

preco = float(input('Informe o valor do produto : '))

print(f'Novo preço do produto foi : {preco - (preco * 0.05)}')
