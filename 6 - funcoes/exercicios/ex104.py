"""
    Crie um programa que tenha a função leiaInt(), que vai funcionar de forma
    semelhante á função input() do Python, só que fazendo a validação para
    aceitar apenas um valor numérico.
      Ex.: n = leiaInt('Digite um n')
"""


def leiaInt(mensagem):
    resultado = False
    valor = 0
    while True:
        numero = str(input(mensagem))
        if numero.isnumeric():
            valor = int(numero)
            resultado = True
        else:
            print('\033[0;31mERRO ! Digite um número inteiro válido.\033[m')
        if resultado:
            break
    return valor


numero = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {numero}')
