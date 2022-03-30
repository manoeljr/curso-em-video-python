"""
    Faça um programa que leia a largura e altura de uma parede em metros.
    Calcule a sua área e a quantidade de tinta necessária para pintá-la.
    Sabendo que cada litro de tinta, pinta uma área de 2 metros quatrados.
"""

largura = float(input('Informe a largura da parede : '))

altura = float(input('Informe a altura da parede : '))

area = largura * altura

print(f'Área de pintura : {area}\n'
      f'Precisa-se de {area / 2} litros de tinta para pinta toda área da parede')
