"""
    Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
    daqueles que forem pares. Se o valor digitado for impar, desconsidere-o.
"""

soma_numeros_pares = 0

for i in range(0, 6):
    numero = int(input('Digite um número inteiro : '))

    if numero % 2 == 0:
        soma_numeros_pares += numero

print(f'A Soma dos números pares digitados foi {soma_numeros_pares}')
