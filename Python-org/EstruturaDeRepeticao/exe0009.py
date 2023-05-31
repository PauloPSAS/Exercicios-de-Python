"""Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50."""


def numeros_impares1a50():
    for i in range(1, 51, 2):
        if i == 49:
            print(i)
        else:
            print(i, end=' - ')


numeros_impares1a50()
