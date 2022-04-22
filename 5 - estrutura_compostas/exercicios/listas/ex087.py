"""
    Aprimore o desafio anterior, mostrando no final:
     A) A Soma de todos os valores pares digitados
     B) A Soma dos valores da terceira coluna
     C) O Maior valor da segunda linha.
"""
matriz = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
total = 0
soma_valores_linha_3 = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite os valores para a matriz [{linha}x{coluna}]: '))
        if matriz[linha][coluna] % 2 == 0:
            total += matriz[linha][coluna]

for i in range(0, 3):
    soma_valores_linha_3 += matriz[2][i]


print('=' * 10)
print(matriz[0])
print(matriz[1])
print(matriz[2])
print('=' * 10)
print(f'A Soma de todos os valores pares -> {total}')
print(f'A Soma dos valores da terceira linha da matriz -> {soma_valores_linha_3}')
print(f'O Maior valor da segunda linha da matriz -> {max(matriz[1])}')
