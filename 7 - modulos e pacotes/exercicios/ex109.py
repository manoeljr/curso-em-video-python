"""
    Modifique as funções que foram criadas no desafio 107 para que
    elas aceitem um parâmetro a mais, informando se o valor retornado
    por elas vai ser ou não formatado pela função moeda(), desenvolvida
    no desafio 108.
"""
from utilidadesCeV.moeda import metade, dobro, aumentar, diminuir, moeda

valor = float(input('Digite o valor: R$ '))

print(f'A Metade de {moeda(valor)} é {moeda(metade(valor, True))}')
print(f'O Dobro de {moeda(valor)} é {moeda(dobro(valor, True))}')
print(f'O Valor {moeda(valor)} aumentado em 10% temos {moeda(aumentar(valor, 10, True))}')
print(f'O Valor {moeda(valor)} diminuindo em 10% temos {moeda(diminuir(valor, 10, True))}')
