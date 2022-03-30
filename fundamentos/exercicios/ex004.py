"""
    Faça um programa que leia algo pelo teclado e mostre na tela o
    seu tipo primitivo e todas as informações possíveis sobre ele
"""

entrada = input('Digite alguma coisa : ')

print(f'Tipo primitivo {type(entrada)}\n'
      f'Só tem espaço {entrada.isspace()}\n'
      f'É Alfabético {entrada.isalpha()}'
      f'É Numero {entrada.isnumeric()}'
      f'Alfa numerico {entrada.isalnum()}\n'
      f'É Maiusculo {entrada.isupper()}'
      f'É Minusculo {entrada.islower()}'
      f'Está capitalizada {entrada.istitle()}')
