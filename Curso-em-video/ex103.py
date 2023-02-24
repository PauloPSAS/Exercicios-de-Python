def ficha(n='<desconhecido>', g=0):
    print(f'O jogador {n} fez {g} gol(s) no campeonato.')


# Main
nome = str(input('Nome do jogador: ')).strip().capitalize()
gols = str(input('Número de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(g=gols)
else:
    ficha(nome, gols)
