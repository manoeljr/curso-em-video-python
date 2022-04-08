"""
    Escreva um programa que leia um número N inteiro qualquer e mostre na tela
    os N primeiros elementos de um sequência de Fibonacci.
    Ex.: 0->1->1->2->3->5->8
"""
print('=' * 30)
print('Seguência de Fibonacci')
print('=' * 30)
numero = int(input('Quantos termos você quer mostrar ? '))
termo_1 = 0
termo_2 = 1
print('~' * 30)
print(f'{termo_1} -> {termo_2}', end='')
cont = 3
while cont <= numero:
    termo_3 = termo_1 + termo_2
    print(f' -> {termo_3}', end='')
    termo_1 = termo_2
    termo_2 = termo_3
    cont += 1
print(' -> FIM')
