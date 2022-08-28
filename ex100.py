from random import randint
from time import sleep


def soma_par(l):
    c = 0
    for v in l:
        if v % 2 == 0:
            c += v
    print(c)


def sorteia(l):
    for cont in range(0, 5):
        l.append(randint(0, 20))
        print(l[cont], end=' ')
        sleep(.5)
    print('PRONTO!')


lista = list()
print('Sorteando 5 valores da lista: ', end='')
sorteia(lista)
print(f'Somando os valores pares de {lista}, temos ', end='')
sleep(1)
soma_par(lista)
