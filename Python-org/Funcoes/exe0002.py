"""Faça um programa para imprimir:
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
para um 'n' informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha."""


def func(a):
    i = 1
    while i <= a:
        for n in range(1, i+1):
            print(n, end=" ")
        print("")
        i += 1


value = int(input("Digite um número inteiro: "))
func(value)
