"""
    Crie um programa onde o usuário possa digitar 7 valores
    númericos e cadastre-os em uma lista única que mantenha separados
    os valores pares e impares. No final, mostre os valores pares e impares
    em ordem crescente.
"""
valores = []
pares = []
impares = []

for valor in range(0, 7):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        pares.append(numero)
    elif numero % 2 == 1:
        impares.append(numero)

valores.append(pares)
valores.append(impares)

print(f'Valores pares -> {sorted(valores[0])}')
print(f'Valores impares -> {sorted(valores[1])}')
