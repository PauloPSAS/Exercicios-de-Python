# Faça um Programa que leia três números e mostre o maior deles.
def maior(x):
    print("O maior é: {}".format(x))


a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
c = int(input("Digite o último número: "))
if b < a > c:
    maior(a)
elif a < b > c:
    maior(b)
elif b < c > a:
    maior(c)
else:
    print("São iguais.")

