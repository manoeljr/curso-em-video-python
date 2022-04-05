"""
    Faça um programa que leia o peso de cinco pessoas.
    No final, mostre qual foi o maior e o menor peso
    lidos.
"""

pesos = []

for pessoa in range(1, 6):
    pessoa = float(input('Informe um peso : '))
    pesos.append(pessoa)

print(f'O Maior peso lido foi {max(pesos)}Kg e o menor foi {min(pesos)}Kg')
