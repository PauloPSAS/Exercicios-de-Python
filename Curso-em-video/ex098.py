from time import sleep


def listras():
    print("-=" * 20)


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    listras()
    print(f"Contagem de {i} a {f} de {p} em {p}.")
    sleep(.7)

    if i < f:
        cont = i
        while cont <= f:
            print(cont, end=' ', flush=True)
            cont += p
            sleep(.7)
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(cont, end=' ', flush=True)
            cont -= p
            sleep(.7)
        print('FIM!')


# Main
contador(1, 10, 1)
contador(10, 0, 2)
listras()
print("Agora é sua vez de personalizar a contagem!")
inicio = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contador(inicio, fim, passo)
