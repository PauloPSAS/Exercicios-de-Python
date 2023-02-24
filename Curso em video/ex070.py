print('\033[34m--' * 20)
print('\033[1;33m{:-^40}\033[m'.format(' LOJÃO SUPER BARATÃO '))
print('\033[34m--' * 20)
total = maior1000 = vbarato = cont = 0
barato = ''
while True:
    nome = str(input('\033[35m\nNome do Produto: '))
    valor = float(input('Preço: R$ '))
    total += valor
    cont += 1
    if valor > 1000:
        maior1000 += 1
    if cont == 1:
        vbarato = valor
        barato = nome
    else:
        if valor < vbarato:
            vbarato = valor
            barato = nome
    continua = str(input('Quer continuar? [S/N] ')).upper().strip()
    while continua != 'S' and continua != 'N':
        print('Digite apenas [S/N] para "SIM" ou "NÃO"')
        continua = str(input('Quer continuar? [S/N] ')).upper().strip()
    if continua == 'N':
        break
print('\033[1;33m{:-^40}'.format(' FIM DO PROGRAMA '))
print('\033[34m--' * 20)
print(f'\033[1;33mO valor total de compras foi: R${total}')
print(f'Temos {maior1000} produto(s) custando mais de R$1000.00')
print(f'O produto mais barato foi "{barato}" que custa R${vbarato:.2f}')
print('\033[34m--' * 20)
