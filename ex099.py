from random import randint
from time import sleep


def maior(*num):
    m = c = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in num:
        print(valor, end=' ')
        sleep(.3)
        if valor > m:
            m = valor
        c += 1
    print(f'Foram informado(s) {c} valor(es) ao todo.')
    print(f'O maior valor informado foi {m}.')


maior(randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20))
maior(randint(0, 20), randint(0, 20), randint(0, 20),)
maior(randint(0, 20), randint(0, 20),)
maior(randint(0, 20))
maior()