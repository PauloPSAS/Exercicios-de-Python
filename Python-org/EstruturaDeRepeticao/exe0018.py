"""Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores."""

from time import sleep


def gera_valores(t):
    import random

    lista = list()
    for num in range(0, t):
        lista.append(random.randint(1, 99))
    return lista


def maior(li):
    m = max(li)
    return m


def menor(li):
    m = min(li)
    return m


def soma(li):
    total = 0
    for num in li:
        total += num
    return total


print("Sequência aleatória de números.")
sleep(.8)
tam = int(input("Digite qual é o tamanho da sequência: "))
valores = gera_valores(tam)
sleep(.8)
print("\nLISTA GERADA: ", end='')
for n in valores:
    print(n, end=' ')
sleep(.6)
print("\n\nO maior valor da lista é: ", end='')
print(maior(valores))
sleep(.6)
print("O menor valor da lista é: ", end='')
print(menor(valores))
sleep(.6)
print("A soma dos valores da lista é: ", end='')
print(soma(valores))
