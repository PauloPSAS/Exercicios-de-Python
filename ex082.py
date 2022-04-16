lista = []
lista_impar = []
lista_par = []
while True:
    lista.append(int(input('\nDigite um número: ')))
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()
    while resp not in 'SsNn':
        print('Digite apenas [S/N] para SIM ou NÃO')
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()
    if resp in 'Nn':
        break
for i, l in enumerate(lista):
    if lista[i] % 2 == 0:
        lista_par.append(l)
    else:
        lista_impar.append(l)
print('=-' * 25)
print(f'A lista completa é {lista}.')
print(f'A lista de pares é {lista_par}')
print(f'A lista de ímpares é {lista_impar}')
