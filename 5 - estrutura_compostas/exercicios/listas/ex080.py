"""
    Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os
    em uma lista, já na posição correta de insersão(sem usar o sort())
    No final, mostre a lista ordenada na tela.
"""
valores = []

for valor in range(0, 5):
    numero = int(input('Digite um número: '))

    if valor == 0 or numero > valores[-1]:
        valores.append(numero)
    else:
        pos = 0
        while pos < len(valores):
            if numero <= valores[pos]:
                valores.insert(pos, numero)
                break
            pos += 1

print(f'Os valores digitados em ordem foram -> {valores}')

