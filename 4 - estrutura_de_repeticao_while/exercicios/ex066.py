"""
    Crie um programa que leia vários números inteiros pelo teclado.
    O Programa só vai parar quando o  usuário digitar o valor 999,
    que é a condição de parada. No final, mostre quantos números foram
    digitados e qual foi a soma entre eles (desconsiderando o flag).
"""
soma = cont = 0

while(True):
    numero = int(input('Digite um número inteiro: '))

    if numero == 999:
        break

    soma += numero
    cont += 1

print(f'Foram digitados {cont} números e a soma foi {soma}')
