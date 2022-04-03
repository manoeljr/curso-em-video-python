"""
    Faça um programa que leia três números e mostre qual é o MAIOR
    e qual é o MENOR
"""
primeiro_valor = int(input('Digite o primeiro valor : '))
segungo_valor = int(input('Digite o segundo valor : '))
terceiro_valor = int(input('Digite o terceiro valor : '))

numeros = [primeiro_valor, segungo_valor, terceiro_valor]

print(f'O Maior valor foi {max(numeros)} e o Menor foi {min(numeros)}')


