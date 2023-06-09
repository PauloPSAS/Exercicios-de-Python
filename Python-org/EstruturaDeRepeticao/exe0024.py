"""Faça um programa que calcule o mostre a média aritmética de N notas."""


def media(n, q):
    t = 0
    for nota in n:
        t += nota
    t /= q
    return t


def criar_notas(qtd):
    notas = []
    for i in range(1, qtd + 1):
        notas.append(float(input(f'Digite a {i} nota: ')))
    return notas


qtdNotas = int(input('Digite quantas Notas serão feitas: '))
valores = criar_notas(qtdNotas)
print(f"\nA média das Notas {valores} é {media(valores, qtdNotas):.1f}.\n")
