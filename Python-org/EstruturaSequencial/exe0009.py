"""Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius."""


def celcius(f):
    c = 5 * ((f - 32) / 9)
    return c


fahrenheit = float(input("Digite a temperatura em Fahrenheit: °F "))
t = celcius(fahrenheit)
print(f"{fahrenheit:.1f}°F equivale à {t:.1f}°C.")
