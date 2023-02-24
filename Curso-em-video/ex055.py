pesado = 0
maneiro = 0
for c in range(1, 6):
    peso = float(input('Peso da %dª pessoa: Kg ' % c))
    if c == 1:
        pesado = peso
        maneiro = peso
    else:
        if peso > pesado:
            pesado = peso
        if peso < maneiro:
            maneiro = peso
print('O maior peso foi de %.1fKg' % pesado)
print('O menor peso foi de %.1fKg' % maneiro)
