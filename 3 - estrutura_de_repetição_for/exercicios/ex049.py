"""
    Refaça o desafio 009, mostrando a tabuada de um número que o usuário
    escolhar, só que agora utilizando um laço FOR.
"""
numero = int(input('Digite um número para a tabuada de multiplicação : '))

print(f'Tabuada de Multiplicação por {numero}')
print('=' * 15)

for i in range(0, 10):
    print(f'{numero} x {i} = {numero * i}')

print('=' * 15)
