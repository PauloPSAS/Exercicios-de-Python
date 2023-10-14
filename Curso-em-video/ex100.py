from time import sleep


def sorteia_num(lista):
    from random import randint

    print("Sorteando 5 valores da lista: ", end='', flush=True)
    sleep(.5)
    for n in range(0, 5):
        lista.append(randint(0, 99))
        print(lista[n], end=' ', flush=True)
        sleep(.5)
    print("PRONTO!")


def soma_par(lista):
    s = 0
    for n in lista:
        if n % 2 == 0:
            s += n
    sleep(1)
    print(f"Somando os valores pares de {lista}, temos {s}.")


num = list()
sorteia_num(num)
soma_par(num)
