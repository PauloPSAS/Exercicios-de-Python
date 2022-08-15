from random import randint
from time import sleep
from operator import itemgetter

print('==' * 20)
ranking = list()
jogadores = {
    'Jogador1': randint(1, 6),
    'Jogador2': randint(1, 6),
    'Jogador3': randint(1, 6),
    'Jogador4': randint(1, 6)}
print('Valores sorteados:')
for k, v in jogadores.items():
    sleep(.8)
    print(f'{k} tirou {v} no dado.')
print('==' * 20)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print(f'{"== RANKING DOS JOGADORES ==":^40}')
for i, v in enumerate(ranking):
    print(f' {i + 1}º lugar: {v[0]} com {v[1]}.')
    sleep(.8)