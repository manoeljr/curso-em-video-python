"""
    Crie um programa que leia o nome de uma cidade e diga se ela
    começa ou não com nome "SANTO".
"""
nome_cidade = input('Digite o nome de um cidade : ')

resultado = nome_cidade.startswith('SANTO')

print(resultado)