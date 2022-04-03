"""
    Crie um programa que leia o nome completo de uma pessoa e mostre:
     - O Nome com todas as letras maiúsculas
     - O Nome com todas minúsculas
     - Quantas letras no total(sem considerar espaços).
     - Quantas letras tem o primeiro nome.
"""

nome = input('Informe seu nome completo : ')

print('Nome com as letras em maiúsculas -> ', nome.upper())
print('Nome com as letras minúsculas -> ', nome.lower())
nome_sem_espacos = nome.rstrip()
nome_sem_espacos = nome.lstrip()
nome_sem_espacos = nome.replace(" ", "")
print(f'Quantas letras no total sem espaços ? R: {len(nome_sem_espacos)} letras')
print(f'Quantas letras tem o primeiro nome ? R: {len(nome.split(" ")[0])} letras')
