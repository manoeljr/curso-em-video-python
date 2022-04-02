"""
    Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO
"""
from datetime import date

ano = int(input('Digite um ano para verificamos se é BISSEXTO ou Não e ZERO para o ano atual : '))
ano_atual = date.today().year

if ano == 0:
    print(f'O Ano é {ano_atual}')
elif ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O Ano {ano} é BISSEXTO')
else:
    print(f'O Ano {ano} não é BISSEXTO')


