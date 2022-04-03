"""
    Escreva um programa que leia dois números inteiros e compare-os,
    mostrando na tela uma mensagem:
     - O Primeiro valor é maior
     - O Segundo valor é maior
     - Não existe valor maior, os dois são iguais
"""
numero_um = int(input('Digite o primeiro número :'))
numero_dois = int(input('Digite o segundo número : '))

if numero_um > numero_dois:
    print(f'O Primeiro número é maior')
elif numero_dois > numero_um:
    print('O Segundo número é maior')
else:
    print('Não existe número maior ou menor. Eles são iguais !')
