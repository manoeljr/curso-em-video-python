"""
    Crie um programa que vai ler vários números e colocar em uma lista.
    Depois disso, crie duas listas extras que vão conter apenas os valores
    pares e os valores impares digitados, respectivamente. Ao final, mostre
    o conteúdo das três listas geradas.
"""
numeros = []
pares = []
impares = []

while True:
    numero = int(input('Digite um número: '))
    resposta = str(input('Digitar outro número ? [S/N]'))
    numeros.append(numero)

    if numero % 2 == 0:
        pares.append(numero)

    elif numero % 2 == 1:
        impares.append(numero)

    if resposta in 'Nn':
        break

print(f'Lista dos números digitados -> {numeros}')
print(f'Lista dos números pares -> {pares}')
print(f'Lista dos números impares -> {impares}')
