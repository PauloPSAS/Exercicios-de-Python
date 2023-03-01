"""Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit."""


def fahrenheit(c):
    fa = (c * 9 / 5) + 32
    return fa


c = float(input("Digite a temperatura em graus Celcius: °C "))
f = fahrenheit(c)
print(f"{c:.1f}°C equivale à {f:.1f}°F.")
