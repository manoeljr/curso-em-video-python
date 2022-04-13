"""
    Desenvolva um programa que leia quatro valores pelo teclado e guarde-os
    em um tupla. No final, mostre:
     A) Quantas vezes apareceu o valor 9
     B) Em que posição foi digitado o primeiro valor 3
     C) Quais foram os números pares
"""
valores = []
numeros_pares = []
cont_nove = 0

for numero in range(4):
    valores.append(int(input('Digite um número: ')))

valores = tuple(valores)

for i in valores:
    if i == 9:
        cont_nove += 1
    elif i % 2 == 0:
        numeros_pares.append(i)

print(f'Quantas vezes apareceu o número 9 -> {cont_nove}')
print(f'Primeiro número 3 localiza-se na posição -> {valores.index(3) + 1}')
print(f'Os números pares foram -> {numeros_pares}')
