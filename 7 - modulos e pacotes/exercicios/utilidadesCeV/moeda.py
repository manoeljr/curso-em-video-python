def aumentar(valor=0, taxa=0, formatado=False):
    resultado = valor + (valor * taxa / 100)
    return resultado if formatado is False else moeda(resultado)


def diminuir(valor=0, taxa=0, formatado=False):
    resultado = valor - (valor * taxa / 100)
    return resultado if formatado is False else moeda(resultado)


def dobro(valor=0, formatado=False):
    resultado = valor * 2
    return resultado if formatado is False else moeda(resultado)


def metade(valor=0, formatado=False):
    resultado = valor / 2
    return resultado if formatado is False else moeda(resultado)


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:>8.2f}'.replace('.', ',')


def resumo(valor=0, taxaA=10, taxaR=0):
    print('-' * 30)
    print('RESMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Dobro do valor: \t{dobro(valor, True)}')
    print(f'Metade do valor: \t{metade(valor, True)}')
    print(f'{taxaA}% de aumento: \t{aumentar(valor, taxaA, True)}')
    print(f'{taxaR}% de redução: \t{diminuir(valor, taxaR, True)}')
    print('-' * 30)

