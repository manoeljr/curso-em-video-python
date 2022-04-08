"""
    Faça um programa que leia o sexo de uma pessoa, mais só aceite
    os valores 'M' ou 'F'. Caso esteja errado, peça a digitação
    novamente até ter um valor correto.
"""
sexo = True

while(sexo):
    print('Digite o sexo : [M/F}')
    sexo = str(input('Qual o sexo : '))

    if sexo in 'Mm' or sexo in 'Ff':
        sexo = False
        break
    else:
        print('Sexo errada !')
        continue
