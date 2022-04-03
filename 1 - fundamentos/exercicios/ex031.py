"""
    Desenvolvar um programa que pergunte a distância de um viagem em Km.
    Calcule o preço da passagem, cobrando R$0.50 por Km para viagens de
    áte 200Km e R$0.45 para viagens mais longas.
"""

distancia = float(input('Digite a distância da viagem : '))
preco = 0

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print(f'A Distância da viagem é {distancia}Km. O Valor da passagem é R${preco}')

# Outra forma de resolver o mesmo problema ============================================
print('==================== Outra forma de resolver o mesmo problema ==================')
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print(f'A Distância da viagem é {distancia}Km. O Valor da passagem é R${preco}')