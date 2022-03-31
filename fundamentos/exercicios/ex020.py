"""
    O Mesmo professor do desafio anterior quer sortear a ordem de apresentação de
     trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e
     mostre a ordem sorteada.
"""
from random import choice, shuffle

primeiro_nome = input('Digite nome : ')
segundo_nome = input('Informe o segundo nome : ')
terceiro_nome = input('O Terceiro nome : ')
quarto_nome = input('O Quarto nome : ')

alunos = [primeiro_nome, segundo_nome, terceiro_nome, quarto_nome]
shuffle(alunos)

print(f'Nome escolhido foi {choice(alunos)}')

