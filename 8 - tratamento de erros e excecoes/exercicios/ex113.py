"""
    Reescreva a função leiaInt() que fizemos no desafio 104, incluindo
    agora a possibilidade da digitação de um número de tipo inválido.
    Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
"""


def leia_int(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
        except(ValueError, TypeError):
            print('\033[31mERRO ! Por favor, digite um número inteiro válido.\033[31m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mEntrada de dados interropida pelo usuário.\033[31m')
            break
        else:
            return numero


def leia_float(mensagem):
    while True:
        try:
            numero = float(input(mensagem))
        except(ValueError, TypeError):
            print('\033[31mERRO ! Por favor, digite um número inteiro válido.\033[31m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mEntrada de dados interropida pelo usuário.\033[31m')
            break
        else:
            return numero


# Número inteiro
numero_inteiro = leia_int('Digite um número inteiro: ')
print(f'Você acabou de digitar o número {numero_inteiro}')

# Número flutuante
numero_flutuante = leia_float('Digite um número flutuante: ')
print(f'Você acabou de digitar o número {numero_flutuante}')
