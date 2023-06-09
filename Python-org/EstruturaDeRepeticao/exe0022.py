"""Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais
número ele é divisível."""


def primo(num):
    total = 0
    divisiveis = list()
    for c in range(1, num + 1):
        if num % c == 0:
            divisiveis.append(num / c)
            total += 1
    if total == 2:
        print("\033[34m{} é um NÚMERO PRIMO.".format(num))
    else:
        print("\033[31m{} não é um NÚMERO PRIMO.\033[m".format(num))
        print("Ele é divisivel por: ", end='')
        for num in divisiveis:
            print(f'{num:.0f}', end=' ')


numero = int(input("Digite um número inteiro: "))
primo(numero)
