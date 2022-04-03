"""
    Desenvolva uma lógica que leia o peso e altura de uma pessoa. Calcule seu IMC e mostre seu status,
    de acordo com a tabela abaixo:
     - Abaixo de 18.5: Abaixo do peso
     - Entre 18.5 e 25: Peso ideal
     - 25 até 30: Sobrepeso
     - 30 até 40: Obesidade
     - Acima de 40: Obesidade mórbida
"""
peso = float(input('Informe o peso Kg: '))
altura = float(input('Informe a altura (m): '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'Abaixo do peso. IMC = {round(imc, 1)}')
elif 18.5 <= imc < 25:
    print(f'Peso ideal. IMC = {round(imc, 1)}')
elif 25 <= imc < 30:
    print(f'Sobrepeso. IMC = {round(imc, 1)}')
elif 30 <= imc < 40:
    print(f'Obesidade. IMC = {round(imc, 1)}')
else:
    print(f'Obesidade mórbida. IMC = {round(imc, 1)}')
