"""
    Crie um programa que simule o funcionamento de um caixa eletrônico.
    No inicio, pergunte ao usuário qual será o valor a ser sacado(número inteiro)
    e o programa vai informar quantas células de cada valor serão entregues.
      OBS.: Considere que o caixa possui cédulas de R$100, R$50, R$20, R$10, R$5, R$2 e R$1.
"""
from time import sleep

print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)

valor = int(input('Informe o valor a ser sacado: '))

montante = valor
cedula = 100
total_de_cedula = 0

while True:
    if montante >= cedula:
        montante -= cedula
        total_de_cedula += 1
    else:
        if total_de_cedula > 0:
            print(f'Total de {total_de_cedula} cédulas de R${cedula}')

        if cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 1

        total_de_cedula = 0
        if montante == 0:
            break

print('=' * 30)
print('Finalizando o programa...')
sleep(2)
