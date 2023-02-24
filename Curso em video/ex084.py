lista = list()
dados = list()
maior = menor = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: Kg ')))
    lista.append(dados[:])

    if len(lista) == 1:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    dados.clear()

    resp = str(input('Quer continuar? [S/N] ')).upper().strip()
    print('\n')
    while resp not in 'SsNn':
        print('Digite apenas [S / N] para Continuar ou parar')
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()
        print('\n')

    if resp in 'Nn':
        break

print('=-=' * 25)
print(f'Você cadastrou {len(lista)} pessoas.')
print(f'O maior peso foi de {maior:.1f}Kg. Que é de ', end='')
for p in lista:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso foi de {menor:.1f}Kg. Que é de ', end='')
for p in lista:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')
