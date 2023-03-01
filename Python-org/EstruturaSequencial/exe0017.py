"""Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em
latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00. Informe ao usuário as
quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias."""

from math import ceil

a = float(input("Digite o tamanho da area em metros quadrados: m² "))
qtdTinta = a / 6
qtdLatas18 = ceil(qtdTinta / 18)
valorLatas = int(qtdLatas18) * 80
qtdgaloes3 = ceil(qtdTinta / 3.6)
valorGaloes = int(qtdgaloes3) * 25
latasP = qtdTinta // 18
resto = qtdTinta % 18
galoesP = ceil(resto / 3.6)
vTB = (latasP * 80) + (int(galoesP) * 25)
desconto = vTB / 100 * 10
vT = vTB - desconto

print()
print(f"\033[33mTamanho da área : {a:.2f}m².")
print(f"Quantidade de tinta necessária em litros(l): {qtdTinta:.2f}l.\n")
print(f"\033[31mComprando só em latas de 18l, será necessário {qtdLatas18:.0f} latas por R$ {valorLatas:.2f}.")
print(f"Comprando só em galões de 3,6l, será necessário {qtdgaloes3:.0f} galões por R$ {valorGaloes:.2f}.")
print("\n\033[1;35mAo comprar misturado você economiza tinta e ganha 10% de desconto!")
print(f"\033[1;34mCompra misturada será necessário {latasP:.0f} latas e {galoesP:.0f} galões. por apenas R$ {vT:.2f}.")
