"""
    Aprimore o DESAFIO 093 para que ele funcione com vários jogadores,
    incluindo um sistema de visualização de detalhes do aproveitamento
    de cada jogador.
"""
time = []
jogador = {}
partidas = []

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    total = int(input(f'Quantas partidas {jogador["nome"]} jogou ?'))
    partidas.clear()

    for contador in range(0, total):
        partidas.append(int(input(f'        Quantos gols na partida {contador + 1} ?')))

    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)

    time.clear(jogador.copy())

    while True:
        resposta = str(input('Quer continuar ? [S/N]')).upper()[0]
        if resposta in 'SN':
            break
        print('ERRO ! Responda apenas S ou N.')
    if resposta == 'N':
        break

print('-=' * 40)
for key, value in enumerate(time):
    print(f'{key:>4 }', end='')
    for d in value.values():
        print(f'{str(d):<15}', end='')
    print()

print('-' * 40)
