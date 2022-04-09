"""
    Crie um programa que leia vários números inteiros pelo teclado. O Programa só vai parar
    quando o usário digitar o valor qqq, que é a condição de parada. No final, mostre quantos
    números foram digitados e qual foi a soma entre eles(desconsiderando o flag.
"""
numero = cont = soma = 0

numero = int(input('Digite um número [999 para parar]: '))

while numero != 999:
    soma += numero
    cont += 1
    numero = int(input('Digite um número [999 para parar]: '))

print(f'Você digitou {cont} números e a soma entre eles foi {soma}.')
