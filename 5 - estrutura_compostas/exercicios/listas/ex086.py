"""
    Faça um programa que crie uma matriz de dimessão 3x3 e
    preencha com valores lidos pelo teclado No final, mostre
    a matriz na tela, com a formatação correta.
"""
matriz = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite os valores para a matriz [{linha}x{coluna}]: '))

print('=' * 10)
print(matriz[0])
print(matriz[1])
print(matriz[2])
