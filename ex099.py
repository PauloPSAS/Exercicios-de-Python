from random import randint

lista = list()


for c in range(0, 5):
    lista.clear()
    mai = 0
    print('-=' * 33)
    print('Analisando valores passados...')
    cont = randint(0, 10)
    if cont == 0:
        print('Foi informado 0 valores a ser passado...')
        print(f'O maior valor informado foi {mai}.')
    else:
        for n in range(0, cont):
            lista.append(randint(0, 20))
            print(lista[n], end=' ')
            if lista[n] > mai:
                mai = lista[n]
        print(f'Foram informado(s) ao todo {len(lista)} valor(es).')
        print(f'O maior valor informado foi {mai}.')
