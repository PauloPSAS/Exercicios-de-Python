def soma(*valores):
    t=0
    for valor in valores:
        t+= valor
    print(f'A soma de {valores} é {t}')


soma(1)
soma(3, 5)
soma(5, 7, 8, 14)
