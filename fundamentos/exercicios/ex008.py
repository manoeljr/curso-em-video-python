"""
    Escreva um programa que leia um valor em metros e o
    exiba convertido em centimetros e milimetros
"""

valor = float(input('Digita uma medida em metros : '))

print(f'Valor em metros : {valor}\n'
      f'Em centimetros : {valor * 100}\n'
      f'Em milimentos : {valor * 1000}')
