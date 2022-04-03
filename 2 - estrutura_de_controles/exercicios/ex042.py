"""
    Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo
    será formado:
     - Equilátero: Todos os lados iguais
     - Isósceles: Dois lados iguais
     - Escaleno: Todos os lados diferentes
"""
primeira = float(input('Primeiro lado do triângulo : '))
segunda = float(input('Segundo lado do triângulo : '))
terceira = float(input('Terceiro lado do triângulo : '))

if primeira < segunda + terceira and segunda < primeira + terceira and terceira < primeira + segunda:
    print('Os Segmentos acima podem formar um triângulo ', end='')
    if primeira == segunda == terceira:
        print('equilátero !')
    elif primeira != segunda != terceira != primeira:
        print('escaleno !')
    else:
        print('isósceles !')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')