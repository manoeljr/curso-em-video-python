"""
    Crie um programa que leia a idade e o sexo de várias pessoas. A Cada pessoa cadastrada, o
    programa deverá perguntar se o usuário quer ou não continuar. No final, mostra:
     A) Quantas pessoas tem mais de 18 anos.
     B) Quantos homens foram cadastrados
     C) Quantas mulheres tem menos de 20 anos
"""
from time import sleep

print('=' * 10)
print('Cadastre um pessoa')
print('=' * 10)
total_18_anos = total_de_mulheres_menor_20_anos = total_de_homens = 0

while True:

    idade = int(input('Idade: '))
    sexo = ' '

    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]

    if idade >= 18:
        total_18_anos += 1

    if sexo == 'M':
        total_de_homens += 1

    if sexo == 'F' and idade < 20:
        total_de_mulheres_menor_20_anos += 1

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar [S/N] ? ')).strip().upper()[0]

    if resposta == 'N':
        print('Saindo do programa...')
        sleep(2)
        print('Até a próxima !')
        break

print(f'Total de pessoas com mais de 18 anos: {total_18_anos}')
print(f'Total de homens cadastrados: {total_de_homens}')
print(f'Total de mulheres com menos de 18 anos: {total_de_mulheres_menor_20_anos}')
