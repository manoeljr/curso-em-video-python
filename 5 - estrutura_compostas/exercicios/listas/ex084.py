"""
    Faça um programa que leia nome e peso de vários pessoas, aguardando tudo em
    uma lista. No final mostre:
     A) Quantas pessoas foram cadastradas.
     B) Uma listagem com as pessoas mais pesadas.
     C) Uma listagem com as pessoas mais leves.
"""
pessoas = []
pessoa = []
total_de_pessoas = 0
maior = menor = 0

while True:
    nome = str(input('Digite o nome: '))
    peso = float(input('Digite a peso: '))
    pessoa.append(nome)
    pessoa.append(peso)

    if len(pessoas) == 0:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]

    pessoas.append(pessoa[:])
    pessoa.clear()
    total_de_pessoas += 1

    resposta = str(input('Deseja informa mais uma pessoa ? [S/N]')).split()[0]

    if resposta in 'Nn':
        break

print()
print('=' * 30)
print(f'{total_de_pessoas} pessoas cadastrada.')
print(f'Lista de pessoas mais pesadas com {maior}Kg. Pessoas -> ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'Lista de pessoas mais leves com {menor}Kg. Pessoas -> ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
