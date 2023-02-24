cont = 'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', \
       'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte'

while True:
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        print('Tente Novamente. ', end='')
    print(f'O número digitado é "{cont[num]}"\n')
    sn = str(input('Quer Continuar? [S/N] ')).upper().strip()
    while sn != 'S' and sn != 'N':
        print('ESCOLHA APENAS [S/N].')
        sn = str(input('Quer Continuar? [S/N] ')).upper().strip()
    if sn == 'N':
        break
print('{:-^40}'.format('FIM DO CÓDIGO'))
