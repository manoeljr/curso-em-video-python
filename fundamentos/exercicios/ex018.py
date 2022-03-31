"""
    Faça um programa que leia um ângulo qualquer e mostre na tela
    o valor do seno, cosseno e tangente desse ângulo.
"""
from math import sin, cos, tan, radians

angulo = float(input('Digite o ângulo: '))
seno = sin(radians(angulo))  # Não estava conseguindo pois tinha esquecido de converte o grau para radiano.
coseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('Ângulo {}º'.format(angulo))
print('Seu Seno é {:.2f}'.format(seno))
print('Seu coseno é {:.2f}'.format(coseno))
print(('Sua Tangente é {:.2f}'.format(tangente)))