"""Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de
arredondamento."""

num = float(input("Digite um número inteiro ou décimal qualquer: "))

if num == round(num):
    print(f"{num} é um número inteiro.")
else:
    print(f"{num} é um número decimal.")
