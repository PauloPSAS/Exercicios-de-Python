"""Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a
decisão é sempre pelo mais barato."""

p1 = float(input("Qual valor do 1° produto: R$ "))
p2 = float(input("Qual valor do 2° produto: R$ "))
p3 = float(input("Qual valor do 3° produto: R$ "))

barato = p1
if p2 < barato:
    barato = p2
if p3 < barato:
    barato = p3
print(f"\nVocê deve comprar o que custa R$ {barato:.2f}.")
