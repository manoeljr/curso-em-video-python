"""
    Elabore um programa que calcule o valor a ser pago por um produto,
    considerando o seu preço normal e condição de pagamento:
     - Á vista dinheiro/cheque: 10% de desconto
     - Á vista no cartão: 5% de desconto
     - Em até 2x no cartão: preço normal
     - 3x ou mais no cartão: 20% de juros
"""
preco = float(input('Qual o valor das compras R$: '))

print('''INFORME A FORMA DE PAGAMENTOS
[ 1 ] á vista dinheiro/cheque
[ 2 ] á vista cartão 
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao_pagamento = int(input('Qual a opção ? '))

if opcao_pagamento == 1:
    desconto = preco - (preco * 0.10)
    print(f'10% de desconto no produto á vista dinheiro/cheque, novo valor do produto R${desconto}')
elif opcao_pagamento == 2:
    desconto = preco - (preco * 0.05)
    print(f'5% de desconto no produto á vista no cartão, novo valor do produto R${desconto}')
elif opcao_pagamento == 3:
    print(f'Valor em até 2x no cartão. Valor do produto R${preco}')
else:
    juro = preco + (preco * 0.20)
    print(f'20% de acrescimo em compras em 3x ou mais no cartão. Novo valor do produto R${juro}')
