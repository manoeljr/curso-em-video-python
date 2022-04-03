"""
    Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
    Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome
    do escolhido.
"""

from random import choice

primeiro_nome = input('Digite nome : ')
segundo_nome = input('Informe o segundo nome : ')
terceiro_nome = input('O Terceiro nome : ')
quarto_nome = input('O Quarto nome : ')

alunos = [primeiro_nome, segundo_nome, terceiro_nome, quarto_nome]

print(f'Nome escolhido foi {choice(alunos)}')
