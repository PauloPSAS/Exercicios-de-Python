"""Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio
gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um."""


def media_gasta(values):
    t = 0
    for c in values:
        t += c
    t /= len(values)
    return t


def in_put():
    cdValues = list()
    qtd = int(input("Digite quantos Cds foi comprado: "))

    for cd in range(1, qtd + 1):
        cdValues.append(float(input(f"Quanto custou o {cd}º Cd? R$ ")))

    return qtd, cdValues


quantidade, valoresCd = in_put()

print(f"\nForam comprado(s) {quantidade} Cd(s).")
print(f"O valor de cada cd foi: ", end='')
for cd in valoresCd:
    print(f"R$ {cd:.2f} ", end='')
print(f"\nFoi gasto em média por cada Cd um total de R$ {media_gasta(valoresCd):.2f}.")
