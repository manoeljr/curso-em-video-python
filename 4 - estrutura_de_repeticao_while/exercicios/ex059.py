"""
    Crie um programa que leia dois valores e mostre um menu na tela:

    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa

    Seu programa deverá realizar a operação solicitada em cada caso.
"""
from time import sleep

opcao = 4

while(opcao):

    print('Digite os números para as operações : ')

    primeiro = float(input('Digite o primeiro valor : '))
    segunda = float(input('Digite o segundo valor : '))

    print()
    print('Escolha sua opção : ')
    print('''
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa
    ''')

    opcao = int(input('Qual a opção : '))

    if opcao == 1:
        print(f'A Soma dos dois valores foi {primeiro + segunda}')
        break
    elif opcao == 2:
        print(f'A Multiplicação dos dois valores foi {primeiro * segunda}')
        break
    elif opcao == 3:
        if max(primeiro, segunda):
            print(f'Maior valor em o primeiro e segundo foi {max(primeiro, segunda)}')
            break
        else:
            print(f'Não existe número maior')
            continue
    elif opcao == 4:
        continue
    elif opcao == 5:
        print('Saindo do sistema...')
        sleep(2)
        break
    else:
        print('Opção inválida !')
        continue
