"""
    A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
    de um atleta e mostre sua categoria, de acordo com a idade:
     - Até 9 anos: MIRIM
     - Até 14 anos: INFANTIL
     - Até 19 anos: JUNIOR
     - Até 25 anos: SÊNIOR
     - Acima: MASTER
"""
from datetime import date

nascimento = int(input('Digite o ano de nascimento : '))
ano_atual = date.today().year - nascimento

if ano_atual <= 9:
    print('Atleta MIRIM')
elif ano_atual <= 14:
    print('Atleta INFANTIL')
elif ano_atual <= 19:
    print('Atleta JUNIOR')
elif ano_atual <= 25:
    print('Atleta SÊNIOR')
else:
    print('Atleta MASTER')

