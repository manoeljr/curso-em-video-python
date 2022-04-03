"""
    Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
    Para salários superiores a R$1.250,00, Calcule um aumento de 10%. Para os inferiores ou iguais
    o aumento é de 15%.
"""
salario = float(input('Informe o valor do salário : '))

if salario > 1250:
    print(f'Seu salário teve um aumento de 10%. Agora é R${round(salario + (salario * 0.10), 3)}')
else:
    print(f'Seu salário teve um aumento de 15%. Agora é R${round(salario + (salario * 0.15), 3)}')
