"""
    Desenvolva um programa que leia o primeiro termo e a razão de um PA.
    No final, mostre os 10 primeiros termos dessa progressão.
"""

primeiro_termo = int(input('Digite o primeiro termo : '))
razao = int(input('Digite a razão : '))
soma = 0

ultimo = primeiro_termo + ((10 - 1) * razao)
ultimo = ultimo + 1

for i in range(primeiro_termo, ultimo, razao):
    print(i)
    soma = soma + i


