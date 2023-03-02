# Faça um Programa que leia três números e mostre o maior e o menor deles.

a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
c = int(input("Digite o último número: "))

maior = menor = a

if b > maior:
    maior = b
if c > maior:
    maior = c
if b < menor:
    menor = b
if c < menor:
    menor = c
print(f"O maior é: {maior}.")
print(f"O menor é: {menor}.")
