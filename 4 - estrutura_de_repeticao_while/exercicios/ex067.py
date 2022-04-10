"""
    Faça um programa que mostra a tabuada de vários números, um de cada vez,
    para cada valor digitado pelo usuário. O Programa será interrompido
    quando o número solicitado for negativo.
"""
print('Vamos cria um tabuada de multiplicação')
print('=' * 15)

while True:
    numero = int(input('Digite o número inteiro para cria a tabuada: '))

    if numero <= 0:
        print('=' * 10)
        print('Tabuada encerrada, até a próxima !')
        break

    print('=' * 10)
    for i in range(1, 11):
        print(f'{numero} x {i} = {numero * i}')
    print('=' * 10)
