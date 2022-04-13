"""
    Crie um tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro
    de futebol, na ordem de colocação. Depois mostre:
     A) Apenas os 5 primeiros colocados
     B) Os Últimos 4 colocados da tabela
     C) Uma lista com os times em ordem alfabética
     D) Em que posição na tabela está o time da chapecoense
"""
times_campeonato_brasileiro = (
    'Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense', 'América-MG',
    'Atlético-GO', 'Santos', 'Ceará-SC', 'Internacional', 'São Paulo', 'Athletico-PR', 'Cuiabá', 'Juventude',
    'Grêmio', 'Bahia', 'Sport Recife', 'Chapecoense'
)


print(f'Os 5 primeiros colocados do campeonato brasileiro -> {times_campeonato_brasileiro[0:5]}')
print(f'Os 4 últimos colocados do campeonato brasileiro -> {times_campeonato_brasileiro[-4:]}')
print(f'Tabela em ordem alfabética do campeonato brasileiro -> {sorted(times_campeonato_brasileiro)}')
print(f'Chapecoense está na {times_campeonato_brasileiro.index("Chapecoense") + 1} posição do campeonato brasileiro')


