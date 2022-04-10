"""
    Crie um programa que leia o nome e o preço de vários produtos.
    O Programa deverá perguntar se o usuário vai continuar. No
    final, mostre:
      A) Qual é o total gasto na compra.
      B) Quantos produtos custam mais de R$1000.
      C) Qual é o nome do produto mais barato.
"""
from time import sleep

total_gasto_na_compra = quantidade_produto_mais_de_mil = cont = menor_valor_produto = 0
nome_produto_mais_barato = ''

while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço do produto R$: '))
    cont += 1

    total_gasto_na_compra += preco
    if preco > 1000:
        quantidade_produto_mais_de_mil += 1

    if cont == 1:
        menor_valor_produto = preco
        nome_produto_mais_barato = nome
    else:
        if preco < menor_valor_produto:
            menor_valor_produto = preco
            nome_produto_mais_barato = nome


    resposta = ''
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]

    if resposta == 'N':
        print('Programa finalizando...')
        sleep(2)
        break

print(f'O Total da compra foi R${round(total_gasto_na_compra, 4)}')
print(f'{quantidade_produto_mais_de_mil} produtos que custam mais de R$1000')
print(f'O Produto mais barato custa R${round(menor_valor_produto, 4)} e foi {nome_produto_mais_barato}')
