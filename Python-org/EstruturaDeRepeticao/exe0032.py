"""Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120.
A saída deve ser conforme o exemplo abaixo:

    Fatorial de: 5
    5! =  5 . 4 . 3 . 2 . 1 = 120"""


def fatorial(n):
    t = n
    for v in range(n, 0, -1):
        if v != 1:
            t *= (v - 1)
        print(f" {v} .", end='') if v != 1 else print(f" {v} = ", end='')
    print(t)
    print()


numero = int(input("Digite um número inteiro para seu fatorial: "))
print(f"{numero}! = ", end='')
fatorial(numero)
