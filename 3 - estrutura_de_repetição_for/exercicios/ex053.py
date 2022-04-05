"""
    Crie um programa que leia uma frase qualquer e diga se ela é
    um palindromo, desconsiderando os espaços.
    Ex.: Apos a sopa
         A Sacada da casa
         A Torre da derrota
         O Lobo ama o bolo
         Anotaram a data da maratona
"""

frase = str(input('Digite uma frase : ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

if inverso == junto:
    print(f'Temos um palindromo -> {junto} | {inverso}')
else:
    print(f'A Frase digitada não é um palindromo -> {junto} | {inverso}')







