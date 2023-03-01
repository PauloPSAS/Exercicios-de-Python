# Faça um Programa que peça dois números e imprima o maior deles.

a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
print("\n")
if a > b:
    print("{} É MAIOR.".format(a))
elif b > a:
    print("{} É MAIOR.".format(b))
else:
    print("SÃO IGUAIS.")
