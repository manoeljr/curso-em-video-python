"""
    Faça um programa que leia um número qualquer e mostre o
    seu fatorial
    Ex.: 5! = 5*4*3*2*1 = 120
"""
numero = int(input('Digite o número fatorial : '))

for i in range(numero, 0, -1):
    print(f'{i}! = {i}*{i-1} =')