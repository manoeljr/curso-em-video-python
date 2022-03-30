"""
    Desenvolva um programa que leia as duas notas de um aluno,
    Calcule e mostre a sua média.
"""

primeira_nota = float(input('Digite a primeira nota : '))

segunda_nota = float(input('Digite a segunda nota : '))

print(f'Sua primeira e segunda notas : {primeira_nota}, {segunda_nota}\n'
      f'Sua média foi {round((primeira_nota + segunda_nota) / 2, 2)}')
