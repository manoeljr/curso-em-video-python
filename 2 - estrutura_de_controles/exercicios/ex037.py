"""
    Escreva um programa que leia um número inteiro qualquer e peça para o usuário
    escolher qual será a base de conversão:
     - 1 para binário
     - 2 para actal
     - 3 para hexadecimal
"""
numero = int(input('Informe um número inteiro qualquer : '))

print('Escolha uma das opçoes para conversão:\n')
print('[ 1 ] Converter para BINÁRIO\n')
print('[ 2 ] Converter para OCTAL\n')
print('[ 3 ] Converter para HEXADECIMAL\n')

conversao_base = int(input('Digite a opção de conversão :'))

if conversao_base == 1:
    binario = bin(numero)
    print(f'Valor convertido para binário : {binario[2:]}')
elif conversao_base == 2:
    octal = oct(numero)
    print(f'Valor convertido para Octal : {octal[2:]}')
elif conversao_base == 3:
    hexadecimal = hex(numero)
    print(f'Valor convertido para hexadecimal : {hexadecimal[2:]}')
else:
    print('Opção Inválida !')

