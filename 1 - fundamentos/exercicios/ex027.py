"""
    Faça um programa que leia o nome completo de uma pessoa, mostrando em
    seguindo o primeiro e o último nome separadamente.
      Ex.: Ana Maria de Souza
           primeiro = Ana
           último = Souza
"""
nome = input('Digite o nome : ')

print(f'Primeiro nome = {nome.split()[0]} e último = {nome.split()[-1]}')
