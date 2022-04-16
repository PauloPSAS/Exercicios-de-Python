matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for lista in range(0, 3):
    for coluna in range(0, 3):
        matriz[lista][coluna] = int(input(f'Digite um valor para [{lista}, {coluna}]: '))
print('=-=' * 15)
for lista in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[lista][coluna]:^6}]', end='')
    print()
