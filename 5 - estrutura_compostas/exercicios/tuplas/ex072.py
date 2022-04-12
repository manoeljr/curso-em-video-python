"""
    Crie um programa que tenha uma tupla totalmente preenchida com uma
    contagem por extenso, de zero até vinte. Seu programa deverá ler um número
    pelo teclado(entre 0 e 20) e mostrá-lo por extenso.
"""
numeros_por_extenso = (
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco',
    'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
    'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
    'dezessete', 'dezoito', 'dezenove', 'vinte'
)

while True:
    numero_digitado = int(input('Digite um número entre 0 e 20: '))

    if numero_digitado < 0 or numero_digitado > 20:
        continue
    else:
        print(f'O Número digitado foi {numeros_por_extenso[numero_digitado]}')
        break
