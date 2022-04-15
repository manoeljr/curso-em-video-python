"""
    Crie um programa onde o usuário possa digitar vários valores numéricos e
    cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será
    adicionado. No final, serão exibidos todos os valores únicos digitados,
    em ordem crescente.
"""
valores = []

while True:
    valor = int(input('Digite um valor: '))

    if valor in valores:
        print('Valor já existe ! ', end='')
        opcao = str(input('Deseja continua? [S/N]')).strip().upper()[0]

        if opcao == 'S':
            continue
        else:
            break

    valores.append(valor)
    print('Valor adicionado com sucesso. ', end='')
    opcao = str(input('Deseja continua? [S/N]')).strip().upper()[0]

    if opcao == 'S':
        continue
    else:
        break

print(f'Você digitou os valores -> {sorted(valores)}')
