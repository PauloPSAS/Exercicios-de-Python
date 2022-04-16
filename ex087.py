matriz = [[0] * 3, [0] * 3, [0] * 3]
soma = 0
soma_coluna3 = 0
maior = 0
for li in range(0, 3):
    for co in range(0, 3):
        matriz[li][co] = int(input(f'Digite um valor para [{li}, {co}]: '))
        if matriz[li][co] % 2 == 0:
            soma += matriz[li][co]
        if matriz[li][co] == matriz[li][2]:
            soma_coluna3 += matriz[li][co]
print('=-=' * 15)
for li in range(0, 3):
    for co in range(0, 3):
        print(f'[{matriz[li][co]:^7}]', end='')
        if li == 1:
            if matriz[li][co] > maior:
                maior = matriz[li][co]
    print()
print(f'\nA soma de todos os valores pares digitados é: {soma}')
print(f'A soma dos valores das terceiras colunas é: {soma_coluna3}')
print(f'O maior valor da segunda linha é: {maior}')
print('=-=' * 15)
