"""
    Crie um programa que leia nome, sexo e idade de várias pessoas, guardado os dados de cada
    pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
     A) Quantas pessoas foram cadastradas
     B) A Média de idade do grupo
     C) Uma lista com todas as mulheres
     D) Uma lista com todas as pessoas com idade acima da média
"""
pessoa = {}
galera = []
soma = media = 0

while True:

    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))

    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO ! Por favor, digite apenas M ou F')

    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())

    while True:
        resposta = str(input('Quer continuar ? [S/N] ')).upper()[0]
        if resposta in 'SN':
            break
        print('ERRO ! Responda apenas S ou N')

    if resposta == 'S':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma /len(galera)
print(f'B) A média de idade é de {media:5.ef} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'p["nome"] ', end='')
print()
print(f'D) Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('     ', end='')
        for key, value in p.items():
            print(f'{key} = {value}; ', end='')
        print()

print('<< encerrado >>')