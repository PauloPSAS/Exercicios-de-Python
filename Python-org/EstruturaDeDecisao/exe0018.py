"""Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida."""

while True:
    d = int(input("Dia: "))
    m = int(input("Mês: "))
    y = int(input("Ano: "))

    v = False

    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        if 1 <= d <= 31:
            v = True

    elif m == 4 or m == 6 or m == 9 or m == 11:
        if 1 <= d <= 30:
            v = True

    elif m == 2:
        if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
            if d <= 29:
                v = True

        elif d <= 28:
            v = True

    print(f"\n{d}/{m}/{y}")
    if v:
        print("É uma data válida.\n")
    else:
        print("Não é uma data válida.\n")

    c = ''
    while c != 'S' and c != 'N':
        c = str(input("Quer continuar? [S/N] ")).upper()
    if c == 'N':
        break
