"""
    Crie um programa que tenha uma tupla única com nomes de produtos e seus
    respectivos preços, na sequência. No final, mostre uma listagem de preços,
    organizando os dados em forma tabular.
"""
listagem = (
    'macarrão', 2.00,
    'feijão', 10.00,
    'arroz', 5.00,
    'açúcar', 2.50,
    'sal', 1.00,
    'farinha', 4.35
)

print('_' * 40)
print(f'{"Lista de produto e preços":^40} ')
print('_' * 40)
for produto in range(0, len(listagem)):
    if produto % 2 == 0:
        print(f'{listagem[produto]:.<30}', end='')
    else:
        print(f'R${listagem[produto]:>7.2f}')
print('_' * 40)
