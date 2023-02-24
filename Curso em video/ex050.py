from random import randint
soma = 0
for c in range(1, 7):
    valores = randint(1, 100)
    print('%d' % valores, end=' ')
    if valores % 2 == 0:
        soma += valores
print('\n')
print('A soma dos números pares escolhidos são: %d' % soma)
