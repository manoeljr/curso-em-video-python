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


def linha(tamanho=42):
    return '-' * tamanho


def cabecalho(texto):
    print(linha())
    print(texto.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    cont = 1
    for item in lista:
        print(f'\033[33m{cont}\033[33m - \033[34m{item}\033[m')
        cont += 1
    print(linha())
    resposta = leia_int('\033[32mSua opcao: \033[m')
    return resposta
