"""
    Crie um programa que leia nome e duas notas de vários alunos e guarde tudo
    em uma lista composta. No final, mostre um boletim contendo a média de cada
    um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
"""
alunos = []

while True:
    nome = str(input('Nome: '))
    nota_1 = float(input('Nota 1: '))
    nota_2 = float(input('Nota 2: '))
    media = (nota_1 + nota_2) / 2
    alunos.append([nome, [nota_1, nota_2], media])

    resposta = str(input('Deseja continua [S/N]? ')).strip()[0]

    if resposta in 'Nn':
        break

print('=' * 30)
print(f'{"N°.":<4}{"NOME":<10}{"MÉDIA:>8"}')
print('-' * 26)
for i, aluno in enumerate(alunos):
    print(f'{i:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')

while True:
    print('-' * 35)
    opcao = int(input('Mostrar notas de qual aluno ?(999 interrompe)'))
    if opcao == 999:
        print('Finalizando')
        break
    if opcao <= len(alunos) - 1:
        print(f'Notas de {alunos[opcao][0]} são {alunos[opcao][1]}')

print('Final do programa')
