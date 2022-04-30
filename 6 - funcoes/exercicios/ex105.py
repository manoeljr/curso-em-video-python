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
    Função de notas e media de varios alunos
    :param notas: Notas dos alunos
    :param situacao(opcional): Situação do alunos em relação a sua média
    :return: Retorna um dicionário com notas e media do aluno
    """
    retorno = {}
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
