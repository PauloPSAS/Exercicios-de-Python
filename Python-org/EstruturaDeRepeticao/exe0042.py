"""aça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos
seguintes intervalos: [0-25], [26-50], [51-75] e [76-100].
A entrada de dados deverá terminar quando for lido um número negativo."""
lista0a25 = []
lista26a50 = []
lista51a75 = []
lista76mais = []

while True:
    numero = int(input("\nDigite um número positivo (números negativos encerrarão o programa): "))
    if numero < 0:
        break
    else:
        if numero > 75:
            lista76mais.append(numero)
        elif numero > 50:
            lista51a75.append(numero)
        elif numero > 25:
            lista26a50.append(numero)
        else:
            lista0a25.append(numero)

print("valores no intervalo de 0 a 25: ", end='')
if len(lista0a25) > 0:
    lista0a25.sort()
    for value in lista0a25:
        print(value, end=' ')
else:
    print("Vazio")
    del lista0a25

print("\nValores no intervalo de 26 a 50: ", end='')
if len(lista26a50) > 0:
    lista26a50.sort()
    for value in lista26a50:
        print(value, end=' ')
else:
    print("Vazio")
    del lista26a50

print("\nValores no intervalo de 51 a 75: ", end='')
if len(lista51a75) > 0:
    lista51a75.sort()
    for value in lista51a75:
        print(value, end=' ')
else:
    print("Vazio")
    del lista51a75

print("\nValores acima de 75: ", end='')
if len(lista76mais) > 0:
    lista76mais.sort()
    for value in lista76mais:
        print(value, end=' ')
else:
    print("Vazio")
    del lista76mais
