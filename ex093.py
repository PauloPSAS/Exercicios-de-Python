jogador = dict()

total_gols = 0
jogador['nome'] = str(input('Nome do jogador: ')).strip().title()
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
jogador['gols'] = list()
for x in range(0, partidas):
    jogador['gols'].append(int(input(f'Quantos gols na partida {x + 1}? ')))
    total_gols += jogador['gols'][x]
jogador['total de gols'] = total_gols
print('==' * 30)
print(jogador)
print('==' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor: {v}')
print('==' * 30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partida(s).')
for p in range(0, partidas):
    print(f'   => Na partida {p + 1}, fez {jogador["gols"][p]} gol(s)')
print()
