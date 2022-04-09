"""
    Crie um programa que leia vários números interos pelo teclado. No Final da execução,
    mostre a média entre todos os valores e qual foi o maior e menor, valores lidos.
    O Programa deve perguntar ao usuário se ele quer ou não continuar a digitar valore.
"""

resposta = 'S'
media_valores = quantidade = soma = maior = menor = 0

while resposta in 'Ss':
    numero = int(input('Digite um número: '))
    resposta = str(input('Quer continuar ? [S/N] ')).upper().strip()

    soma += numero
    quantidade += 1

    if quantidade == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

media_valores = soma / quantidade
print(f'Você digitou {quantidade} números e a média foi {media_valores}.')
print(f'O Maior valor foi {maior} e o menor foi {menor}')


