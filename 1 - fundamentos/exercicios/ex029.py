"""
    Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
    mostre uma mensagem dizendo que ele foi multado. A Multa vai custar R$7.00 por cada
    Km acima do limite.
"""
velocidade = int(input('Digite a velocidade do veiculo : '))

if velocidade > 80:
    print(f'Velocidade acima de 80Km/h a multa é R${(velocidade - 80) * 7}')

print(f'{velocidade}Km/h velocidade permitida.')

