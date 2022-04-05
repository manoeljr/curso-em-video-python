"""
    Faça um programa que calcule a soma entre todos os números impares que
    são múltiplos de três e que se encontram no intervalo de 1 até 500.
"""

soma_numeros_multiplos_de_tres = 0

for i in range(1, 501, 2):
    if i % 3 == 0:
        soma_numeros_multiplos_de_tres += i

print(f'A Soma de todos os números impares e múltiplos de três : {soma_numeros_multiplos_de_tres}')
