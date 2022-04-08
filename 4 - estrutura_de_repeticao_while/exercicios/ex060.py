"""
    Faça um programa que leia um número qualquer e mostre o
    seu fatorial
    Ex.: 5! = 5*4*3*2*1 = 120
"""
from math import factorial

numero = int(input('Digite o número fatorial : '))
fatorial = 1

# Solução usando modulo do Python
print(f'O Fatorial de {numero} é {factorial(numero)}')
print('-=' * 16)
# Outra forma de desenvolver o fatorial
print(f'Calculando {numero}! = ', end='')
while numero > 0:
    print(f'{numero}', end='')
    print(f' x ' if numero > 1 else ' = ', end='')
    fatorial *= numero
    numero -= 1

print(f'{fatorial}')

