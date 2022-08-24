jogadores = list()
partidas = list()
jogador = dict()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: ')).strip().title()
    jogos = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    
    for c in range(0, jogos):
        partidas.append(int(input(f'    Quantos gols na partida {c + 1}? ')))
    
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(jogador['gols'])
    jogadores.append(jogador.copy())
    partidas.clear()
    
    while True:
        rsp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if rsp in 'SN':
            break
        else:
            print('ERRO! Responda apenas S ou N...')
    if rsp == 'N':
        break

print('==' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('--' * 20)

for k, v in enumerate(jogadores):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('__' * 20)

while True:
    pesquisa = int(input('Mostrar dados de qual jogador? (999 para encerrar) '))
    if pesquisa == 999:
        break
    if pesquisa >= len(jogadores):
        print(f'ERRO! Não existe jogador com o código {pesquisa}!')
    else:
        print(f' __ LEVANTAMENTO DO JOGADOR {jogadores[pesquisa]["nome"]} __ ')
        for i, g in enumerate(jogadores[pesquisa]['gols']):
            print(f'    No jogo {i + 1} fez {g} gol(s).')
        print('--' * 20)
print('<< FIM >>')
