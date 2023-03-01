# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

def area(r):
    from math import pi, pow
    ar = pi * pow(r, 2)
    return ar


raio = float(input("Digite o raio do circulo: "))
a = area(raio)
print(f'A área de um circulo com o raio de {raio:.1f} equivale a {a:.1f}')
