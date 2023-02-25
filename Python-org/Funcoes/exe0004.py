"""Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’,
se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo."""


def func(value):
    if value > 0:
        r = 'P'
        return r
    else:
        r = 'N'
        return r


valor = int(input("Digite um valor: "))
print(func(valor))
