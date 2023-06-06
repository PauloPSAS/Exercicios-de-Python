"""Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo
número. Não utilize a função de potência da linguagem."""


def exponenciaca0(b, e):
    t = 1
    for x in range(e):
        t *= b
    return t


base = int(input("Digite um número inteiro para a base da potência: "))
expoente = int(input("Digite o expoente: "))

print(f"{base}^{expoente}.")

total = exponenciaca0(base, expoente)

for n in range(0, expoente):
    print(f"{base} * ", end='') if n+1 != expoente else print(f"{base} = ", end='')
print(total)
