"""Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá
pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
a) Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir
os demais valores, encerrado;
b) Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
c) Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
d) Se o delta for positivo, a equação possui duas raízes reais; informe-as ao usuário;"""
import sys
from math import sqrt

while True:
    ax = float(input("Digite um número inteiro para ax²: "))
    if ax == 0:
        print("ax² é 0 portanto não é uma equação de segundo grau.")
        sys.exit()
    else:
        break
bx = float(input("Digite um número inteiro para bx: "))
c = float(input("Digite um número inteiro para c: "))

delta = (bx ** 2) - (4*(ax*c))

print("\n")
print(f"Delta é: {delta:.1f}")

if delta < 0:
    print("Delta é negativo portanto não possui resultado real.")
elif delta == 0:
    print("Delta é igual a zero portanto a equação possui apenas um resultado real.")
    x = ((0 - bx) + sqrt(delta)) / (2 * ax)
    print(f"O valor é: {x:.1f}")
else:
    print("Delta é positivo portanto possui duas raízes reais.")
    x = ((0 - bx) + sqrt(delta)) / (2 * ax)
    y = ((0 - bx) - sqrt(delta)) / (2 * ax)
    print("São elas: ")
    print(f"Raiz 1: {x:.1f}\nRaiz 2: {y:.1f}")

