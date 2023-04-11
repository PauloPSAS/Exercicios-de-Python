"""Faça um programa que leia 5 números e informe o maior número."""

import random
import time

maior = 0
numeros = []

for i in range(0, 5):
    numeros.append(random.randint(1, 99))
    if numeros[i] > maior:
        maior = numeros[i]
print("Gerando 5 números aleatórios...")
time.sleep(1)
for i in numeros:
    print(i, end=' ')
time.sleep(1)
print(f"\nO maior é {maior}.")
