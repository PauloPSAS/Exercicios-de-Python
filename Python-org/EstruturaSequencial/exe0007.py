"""Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário."""


def area(l):
    a = l ** 2
    return a


laterais = float(input("Qual vai ser a largura e altura do quadrado: "))
areaQuadrado = area(laterais)
dobroArea = areaQuadrado * 2
print(f"\nUm quadrado com larg e altura de {laterais:.1f}m² tem a area de {areaQuadrado:.1f}m².")
print(f"E o dobro da sua area equivale à {dobroArea:.1f}m².")
