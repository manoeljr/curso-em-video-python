"""
    Faça um programa que leia um número de 0 a 9999 e mostre na tela
    cada um dos digitos separados.
    Ex.: Digite um número: 1834
         unidade: 4
         dezena: 3
         centenas: 8
         milhar: 1
"""

numero = int(input('Digite um número inteiro entre 0 e 9999 : '))

unidade = numero // 1 % 10
dezena  = numero // 10 % 10
centena = numero // 100 % 10
milha   = numero // 1000 % 10

print('Unidades : ', unidade)
print('Dezena : ', dezena)
print('Centenas : ', centena)
print('Milhar : ', milha)
