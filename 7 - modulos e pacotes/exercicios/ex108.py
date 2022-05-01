"""
    Adapte o código do desafio 107, criando uma função adicional
    chamada moeda() que consiga mostrar os valores como um valor
    monetário formatado.
"""
from utilidadesCeV.moeda import metade, dobro, aumentar, diminuir, moeda

valor = float(input('Digite o valor: R$ '))

print(f'A Metade de {moeda(valor)} é {moeda(metade(valor))}')
print(f'O Dobro de {moeda(valor)} é {moeda(dobro(valor))}')
print(f'O Valor {moeda(valor)} aumentado em 10% temos {moeda(aumentar(valor, 10))}')
print(f'O Valor {moeda(valor)} diminuindo em 10% temos {moeda(diminuir(valor, 10))}')
