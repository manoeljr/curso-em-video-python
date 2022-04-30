"""
    Faça um programa que tenha uma função notas() que pode receber várias notas
    de alunos e vai retornar um dicionário com as seguintes informações:
      - Quantidade de notas
      - A maior nota
      - A menor nota
      - A média da turma
      - A situação(Opcional)
    Adicione também as docstrings da função
"""


def notas(*notas, situacao=False):
    """
    Função para analisar notas e situações de vários alunos
    :param notas: Um ou mais notas dos alunos (aceita várias notas)
    :param situacao: Valor opcional, indicando se deve ou não adicionar a situação do aluno
    :return: Retorna um dicionário com várias informações sobre a situação da turma
    """
    retorno = dict()
    retorno['total'] = len(notas)
    retorno['maior'] = max(notas)
    retorno['menor'] = min(notas)
    retorno['media'] = sum(notas) / len(notas)

    if situacao:
        if retorno['media'] >= 7:
            retorno['situacao'] = 'BOA'
        elif retorno['media'] >= 5:
            retorno['situacao'] = 'RAZOAVEL'
        else:
            retorno['situacao'] = 'RUIM'

    return retorno


resposta = notas(9, 10, 5.5, 2.5, 8.5, situacao=True)
print(resposta)
