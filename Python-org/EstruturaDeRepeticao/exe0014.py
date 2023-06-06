"""Faça um programa que peça 10 valores inteiros, calcule e mostre a quantidade de números pares e a quantidade
de números ímpares."""

import random

numeros = []
pares = []
impares = []

for num in range(0, 10):
    numeros.append(random.randint(1, 99))
    if numeros[num] % 2 == 0:
        pares.append(numeros[num])
    else:
        impares.append(numeros[num])

print("Os números escolhidos foram: ", end='')
for num in numeros:
    print(f"{num} ", end='')

print(f"\n\nForam identificados {len(pares)} números pares: ", end='')
for num in pares:
    print(f'{num} ', end='')
print()
print(f"Foram identificados {len(impares)} números ímpares: ", end='')
for num in impares:
    print(f"{num} ", end='')
