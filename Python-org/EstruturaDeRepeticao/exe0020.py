"""Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o
fatorial a números inteiros positivos e menores que 16."""


def valor():
    while True:
        value = int(input("Digite um número para tirar o fatorial: "))
        if value >= 16 or value <= 0:
            print("\nDigite apenas valores maiores que 0 ou menores que 16...")

        else:
            break
    return value


def fatorial(n):
    from math import factorial
    total = factorial(n)
    print(f"{n} != ", end='')
    for i in range(n, -1, -1):
        print(f"{i}", end='')
        if i != 0:
            print('.', end='')
        else:
            print(end=' ')
    print(f"= {total}.")


v = valor()
fatorial(v)
while True:
    y = str(input("\nQuer continuar [S/N]? ")).upper()
    print("")
    if y == "S":
        v = valor()
        fatorial(v)
    elif y == "N":
        print("\nMuito Obrigado por usar este código.")
        break
    else:
        print("Digite apenas 'S' para SIM ou 'N' para NÃO.")
