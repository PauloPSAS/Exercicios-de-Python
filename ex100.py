from random import randint
from time import sleep

lista = list()


def soma_par(l):
    c = 0
    for v in l:
        if v % 2 == 0:
            c += v
    sleep(.5)
    print(c)
    
    
    
def sorteia(l):
    for cont in range(0, 5):
        l.append(randint(0, 9))
        print(l[cont], end=' ')
        sleep(.5)
    print('PRONTO!')


print('Sorteando 5 valores da lista: ', end='')
sorteia(lista)
print(f'Somando os valores pares de {lista}, temos ', end='')
soma_par(lista)
