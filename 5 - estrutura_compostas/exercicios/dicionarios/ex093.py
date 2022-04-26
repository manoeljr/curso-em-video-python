"""
    Crie um programa que gerencie o aproveitamento de um jogador de futebol.
    O Programa vai ler o nome do jogador e quantas partidas ele jogou. Depois
    vai ler a quantidade de gols feitos em cada partida. No final, tudo isso
    será guardado em um dicionário, incluindo o total de gols feitos durante
    o campeonato.
"""
jogador = {}
partidas = []

jogador['nome'] = str(input('Nome do jogador: '))
total = int(input(f'Quantas partidas {jogador["nome"]} jogou ?'))

for contador in range(0, total):
    partidas.append(int(input(f'        Quantos gols na partida {contador + 1} ?')))

jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)

print('-=' * 30)
print(jogador)
print('-=' * 30)
for key, value in jogador.items():
    print(f'O Campo {key} temo valor {value}')

print('-=' * 30)
print(f'O Jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')

for index, value in enumerate(jogador['gols']):
    print(f'     => Na partida {index}, fez {value} gols.')

print(f'Foi um total de {jogador["total"]} de gols.')
