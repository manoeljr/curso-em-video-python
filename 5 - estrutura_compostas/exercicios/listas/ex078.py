"""
    Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
    No final, mostre qual foi o maior e o menor valor digitado e as suas
    respectivas posições na lista.
"""
valores = []

for valor in enumerate(range(5)):
    numero = int(input('Digite um número: '))
    valores.append(numero)

print(f'O Maior valor -> {max(valores)} e seu indice -> {valores.index(max(valores))}.\n '
      f'O Menor valor -> {min(valores)} e seu indice -> {valores.index(min(valores))}.')

