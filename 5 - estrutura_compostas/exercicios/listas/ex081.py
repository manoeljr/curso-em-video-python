"""
    Crie um programa que vai ler vários números e colocar em uma lista.
    Depois disso, mostra:
     A) Quantos números foram digitados
     B) A lista de valores, ordenada de forma decrescente
     C) Se o valor 5 foi digitado e está ou não na lista
"""

numeros = []

while True:
    numero = int(input('Digite um número: '))
    numeros.append(numero)
    resposta = str(input('Quer continuar ? [S/N]')).split()[0]

    if resposta in 'Nn':
        break

print('=' * 30)
print(f'Você digitou {len(numeros)} elementos.')
print(f'Lista ordenada de forma decrescente -> {numeros.sort(reverse=True)}')
print(f'O Valor 5 foi digitado -> {"Sim" if 5 in numeros else "Não"}')
