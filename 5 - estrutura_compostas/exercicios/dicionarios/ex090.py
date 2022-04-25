"""
    Faça um programa que leia nome e média de um aluno,
    guardando também a situação em um dicionário. No final,
    mostre o contéudo da estrutura na tela.
"""

alunos = {}

alunos['nome'] = str(input('Nome: '))
alunos['media'] = float(input('Média:'))

if alunos['media'] >= 7:
    alunos['situacao'] = 'aprovado'
elif 5 <= alunos['media'] < 7:
    alunos['situacao'] = 'recuperação'
else:
    alunos['situacao'] = 'reprovado'

for key, value in alunos.items():
    print(f'{key} é igual a {value}.')
