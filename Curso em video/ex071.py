print('==' * 20)
print('\033[1;33m{:-^40}'.format(' BANCO DO DANONÃO GROSSO \033[m'))
print('==' * 20)
valor = int(input('\033[36mQual valor você quer sacar? R$ '))
total = valor
ced = 200
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'\033[34mTotal de {totced} cédula(s) de R$ {ced}\033[m')
        if ced == 200:
            ced = 100
        elif ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
        elif ced == 2:
            ced = 1
        totced = 0
        if total == 0:
            break
print('==' * 20)
print('\033[1;33m{:^40}'.format('FIM do Código'))

