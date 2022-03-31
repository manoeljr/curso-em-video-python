"""
    Escreva um programa que pergunte a quantidade de KM percorridos por
    um carro alugado e a quantidade de dias pelos quais ele foi alugado.
    Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia
    e R$ 0.15 por KM rodado.
"""

quantidade_km_percorrido = float(input('Informe a quantidade de KM : '))
quantidade_dias_alugado = int(input('Qual a quantidade de dias de aluguel : '))

valor_por_dia = quantidade_dias_alugado * 60
valor_por_km = quantidade_km_percorrido * 0.15
valor_do_alugue = valor_por_dia + valor_por_km

print(f'O Valor do aluguel em {quantidade_dias_alugado} dias foi de R$ {valor_do_alugue}')

