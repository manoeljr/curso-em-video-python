"""
    Faça um programa que leia o sexo de uma pessoa, mais só aceite
    os valores 'M' ou 'F'. Caso esteja errado, peça a digitação
    novamente até ter um valor correto.
"""
#  Uma forma de digitar a sexo
# sexo = True
#
# while(sexo):
#     print('Digite o sexo : [M/F}')
#     sexo = str(input('Qual o sexo : ')).strip().upper()[0]
#
#     if sexo in 'Mm' or sexo in 'Ff':
#         sexo = False
#         break
#     else:
#         print('Sexo errada !')
#         continue

#  Outra forma
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]

while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, Informe seu sexo : ')).strip().upper()[0]

print(f'Sexo {sexo} registrado com sucesso.')

