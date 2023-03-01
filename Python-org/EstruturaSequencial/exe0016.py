"""Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em
latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o
preço total."""

import math

area = float(input("Digite o tamanho da área em metros quadrados: m² "))
qtdTinta = area / 3
qtdLatas = math.ceil(qtdTinta / 18)
valorTinta = 80.00

print(f"Será necessário {qtdTinta:.2f} litro(s) de tinta.")
print(f"Será necessário {qtdLatas:.0f} lata(s) de 18 litro(s) de tinta.")
print(f"O valor total da(s) {qtdLatas:.0f} lata(s) à R$ 80.00 cada é de R$ {qtdLatas * 80.00:.2f}.")
