"""
    Crie um código em Python que teste se o site Pudim está
    acessivel pelo computador usado.
"""


def resposta_site():
    from urllib import request

    try:
        site = request.urlopen('http://www.pudim.com.br')
    except:
        print('Erro ! Não conseguimos acessar o site www.pudim.com.br')
    else:
        print('OK ! O Site está ativo.')


resposta_site()
