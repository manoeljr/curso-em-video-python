"""
    Aprimore o DESAFIO 093 para que ele funcione com vários jogadores,
    incluindo um sistema de visualização de detalhes do aproveitamento
    de cada jogador.
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
