"""Faça um programa para imprimir:

    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n

para um 'n' informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha."""


def func(a):
    i = 1
    while i <= a:
        for n in range(i):
            print(i, end=' ')
        print("")
        i += 1


value = int(input("Digite um número inteiro: "))
func(value)
