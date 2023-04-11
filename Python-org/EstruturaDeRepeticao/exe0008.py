"""Faça um programa que leia 5 números e informe a soma e a média dos números."""

from random import randint
from time import sleep

media = soma = 0
numeros = []

for i in range(0, 5):
    numeros.append(randint(1, 99))
    soma += numeros[i]
media = soma / len(numeros)
print("Gerando valores aleatórios...")
sleep(1)
for i in numeros:
    print(i, end=' ')
sleep(.7)
print(f"\nA soma dos valores gerados é: {soma}")
print(f"A média dos valores gerados é: {media:.1f}")
