"""
    Adicione ao módulo moeda.py criado nos desafios anteriores,
    uma função chamada resumo(), que mostre na tela algumas
    informações geradas pelas funções que já temos no módulo
    criado até aqui,
"""
from utilidadesCeV.moeda import resumo

valor = float(input('Digite o valor: R$'))
resumo(valor, 20, 12)

