"""
    Crie um programa que leia duas notas de um aluno e calcule sua média. Mostrando
    uma mensagem no final, de acordo com a média atingida:
     - Média abaixo de 5.0: REPROVADO
     - Média entre 5.0 e 6.9: RECUPERAÇÃO
     - Média 7.0 ou superior: APROVADO
"""
primeira_nota = float(input('Digite a primeira nota : '))
segunda_nota = float(input('Digite a segunda nota : '))
media = (primeira_nota + segunda_nota) / 2

if media < 5:
    print('REPROVADO')
elif 5 <= media <= 6.9:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')
