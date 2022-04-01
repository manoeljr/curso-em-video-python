"""
    Faça um programa que leia uma frase pelo teclado e mostra:
     - Quantas vezes aparece a letra "A"
     - Em que posição ela aparece a primeira vez
     - Em que posição ela aparece a última vez
"""

frase = str(input('Digite um frase, por favor : ')).upper().strip()

print(f'Aparecem na frase a letra A {frase.count("A")} vezes')

print(f'Primeira letra A aparece na posição {frase.find("A") + 1}')

print(f'Última letra A apareceu na posição {frase.rfind("A") + 1}')
