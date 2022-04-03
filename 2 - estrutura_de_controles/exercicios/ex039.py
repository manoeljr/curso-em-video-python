"""
    Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade.
     - Se ele ainda vai se alistar ao serviço militar.
     - Se é a hora de se alistar
     - Se já passou do tempo do alistamento
    Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""
from datetime import date


ano_nascimento = int(input('Informe seu ano de nascimento : '))
idade = date.today().year - ano_nascimento

if idade == 18:
    print(f'Você tem {idade} anos, já é hora de se alistar ao serviço militar')
elif idade < 18:
    falta_anos_para_alistamento_militar = 18 - idade
    print(f'Falta {falta_anos_para_alistamento_militar} anos para se alistar ao serviço militar')
else:
    passou_anos_alistamento_militar = idade - 18
    print(f'Você já passou {passou_anos_alistamento_militar} anos para se alistar ao serviço militar')

