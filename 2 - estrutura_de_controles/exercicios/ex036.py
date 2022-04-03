"""
    Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
    O Programa vai perguntar o valor da casa, o salário do comprador e em quantos anos
    ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder
    30% do salário ou então o empréstimo será negado.
"""
valor_da_casa = float(input('Valor da casa: R$ '))
salario_comprador = float(input('Qual o valor do salário: R$ '))
quantos_anos_vai_pagar = int(input('Quantos anos vai ser pagar a casa: '))

valor_max_parcela = round(salario_comprador * 0.30, 3)
valor_parcela_emprestimo = round(valor_da_casa / (quantos_anos_vai_pagar * 12), 3)

if valor_parcela_emprestimo >= valor_max_parcela:
    print(f'Valor da parcela R${valor_parcela_emprestimo} excedeu o valor máximo permitido R${valor_max_parcela}. Emprestimo Negado')
else:
    print(f'Emprestimo Consedido ! Ficando {quantos_anos_vai_pagar} anos com parcelas de R${valor_parcela_emprestimo}')

