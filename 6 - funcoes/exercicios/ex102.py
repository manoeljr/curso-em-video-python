"""
    Crie um programa que tenha uma função fatorial() que receba
    dois parâmetro: O primeiro que indique o número a calcular
    e o outro chamado show, que será um valor lógico(opcional)
    indicando se será mostrado ou não na tela o processo de
    cálculo do fatorial.
"""


def fatorial(numero, show=False):
    """
    Calcula o fatorial de um número
    :param numero: O nũmero a ser calculado
    :param show opcional: Mostra ou não a conta
    :return: o fatorial do número
    """
    fatorial = 1
    for cont in range(numero, 0, -1):
        if show:
            print(cont, end='')
            if cont > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        fatorial *= cont
    return fatorial


numero = int(input('Digite o valor do fatorial: '))
show = str(input('Deseja verifica o fatorial [S/N]: ')).upper()[0]
if show in 'Ss':
    print(fatorial(numero, show=True))
else:
    print(fatorial(numero, show=False))

