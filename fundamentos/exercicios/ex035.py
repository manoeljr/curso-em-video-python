"""
    Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas
    podem ou não formar um triângulo.
"""
primeira = float(input('Digite o valor da primeira reta : '))
segunda = float(input('Digite o valor da segunda reta : '))
terceira = float(input('Digite o valor da terceira reta : '))

if primeira < segunda + terceira and segunda < primeira + terceira and terceira < primeira + segunda:
    print('Os Segmentos acima PODEM FORMAR um triângulo')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')

