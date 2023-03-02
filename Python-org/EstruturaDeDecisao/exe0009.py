# Faça um Programa que leia três números e mostre-os em ordem decrescente.

a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
c = int(input("Digite o último número: "))
valores = a, b, c
valores = sorted(valores)
print("Em ordem crescente são: {}, {} e {}.".format(valores[0], valores[1], valores[2]))
