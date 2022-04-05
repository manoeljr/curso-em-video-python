"""
    Crie um programa que leia o ano de nascimento de sete pessoas.
    No final, mostre quantas pessoas ainda não atingiram a maioridade(21 anos)
    e quantos já são maiores.
"""
from datetime import date

ano_atual = date.today().year
pessoas_nao_maioridade, pessoas_maioridade = 0, 0

for pessoa in range(1, 8):
    ano = int(input('Digite o ano que você nasceu : '))

    if ano_atual - ano > 21:
        pessoas_maioridade += 1
    else:
        pessoas_nao_maioridade += 1

print(f'{pessoas_maioridade} pessoas maioridade e {pessoas_nao_maioridade} pessoas não maioridade')
