times = 'Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense', 'América-MG', \
        'Atlético-GO', 'Santos', 'Ceará SC', 'Internacional', 'São Paulo', 'Athletico-PR', 'Cuiabá', 'Juventude', \
        'Grêmio', 'Bahia', 'Sport Recife', 'Chapecoense'

print(f'\033[36mLista dos Times do Brasileirão série A de 2021: {times}\n')
print(f'\33[34mOs 5 primeiros são: {times[:5]}\n')
print(f'\033[31mOs 4 Últimos são: {times[-4:]}\n')
print(f'\033[32mTimes em Ordem Alfabética: {sorted(times)}\n')
print(f'\033[35mO chapecoense está na {times.index("Chapecoense") + 1}ª posição\n')
