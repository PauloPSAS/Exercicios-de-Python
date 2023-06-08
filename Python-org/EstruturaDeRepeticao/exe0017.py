"""Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120"""


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


value = int(input("Digite um número para tirar o fatorial: "))
fatorial(value)
