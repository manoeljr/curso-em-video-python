"""
    Desenvolva um programa que leia o nome, idade e sexo de
    4 pessoas. No final do programa, mostre :
        -> A média de idade do grupo
        -> Qual é o nome do homem mais velho
        -> Quantas mulheres têm menos de 20 anos
"""

soma_idade, media_idade, maior_idade_homem, total_mulher_20_anos = 0, 0, 0, 0
nome_homem_mais_velho = ''

for i in range(1, 5):
    print(f'{i} pessoa' * 10)
    nome = str(input('Digite o nome : ')).strip()
    idade = int(input('Digite sua idade : '))
    sexo = str(input('Digite o sexo [M/F]: ')).strip()
    print()
    soma_idade += idade

    if i == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_homem_mais_velho = nome

    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_homem_mais_velho = nome

    if sexo in 'Ff' and idade < 20:
        total_mulher_20_anos += 1

media_idade = soma_idade / 4
print(f'A Média de idade do grupo é de {media_idade} anos')
print(f'O Homem mais velho tem {maior_idade_homem} anos e se chama {nome_homem_mais_velho}.')
print(f'Ao todo são {total_mulher_20_anos} mulheres com menos de 20 anos.')

