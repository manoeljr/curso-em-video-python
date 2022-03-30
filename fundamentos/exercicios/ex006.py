"""
    Crie um algoritmo que leia um número e mostre o seu
    dobro, triplo e raiz quadrada
"""

numero = int(input('Informe um número :'))

print(f'O Número informado foi {numero}\n'
      f'Seu dobro é {numero * 2}\n'
      f'O Triplo {numero * 3}\n'
      f'Raiz quadrada {round(numero**(1/2), 2)}')
#       Raiz quadrada {:.2f}, duas casas decimas depois da virgula
