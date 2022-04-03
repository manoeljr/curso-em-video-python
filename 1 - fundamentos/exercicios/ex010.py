"""
    Crie um programa que leia quanto dinheiro uma pessoa tem na
    carteira e mostre quantos dólares ela pode comprar.
    Considere o dolar no valor -> U$ 1 = R$ 3.27
"""

valor_em_dinheiro  = float(input('Digite o seu valor em dinheiro R$:'))

print(f'Você pode comprar {valor_em_dinheiro / 3.27} dólar(es)')
