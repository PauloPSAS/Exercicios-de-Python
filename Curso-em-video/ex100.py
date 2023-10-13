def sortear():
    from time import sleep
    from random import randint


    def soma_par(lista):
        s = 0
        sleep(.5)
        print(f"Somando os valores pares de {lista}, temos ", end='')
        for v in lista:
            if v % 2 == 0:
                s += v
        print(s)


    print("Sorteando 5 valores da lista: ", end='')
    valores = []
    for x in range(0, 5):
        valores.append(randint(0, 9))
        sleep(.5)
        print(valores[x], end=' ', flush=True)
    sleep(.5)
    print("PRONTO!")
    soma_par(valores)

sortear()
