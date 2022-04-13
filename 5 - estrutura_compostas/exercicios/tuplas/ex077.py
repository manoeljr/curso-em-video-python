"""
    Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
    Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""
palavras = ('gratis', 'problema')

for palavra in palavras:
    print(f' Na palavra {palavra.upper()} temos ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end='')
