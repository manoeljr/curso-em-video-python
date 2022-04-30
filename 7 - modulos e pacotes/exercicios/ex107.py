"""
    Crie um módulo chamado moeda.py que tenha as funções
    incorporadas aumentar(), diminuir(), dobro(), metade().
    Faça também um programa que importe esse módulo e use
    algumas dessas funções.
"""
from moeda import metade, dobro, aumentar, diminuir

valor = float(input('Digite o valor: R$ '))

print(f'A Metade de {valor} é {metade(valor)}')
print(f'O Dobro de {valor} é {dobro(valor)}')
print(f'O Valor {valor} aumentado em 10% temos R$ {aumentar(valor, 10)}')
print(f'O Valor {valor} diminuindo em 10% temos R$ {diminuir(valor, 10)}')
