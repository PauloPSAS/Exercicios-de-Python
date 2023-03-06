"""Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
Média de Aproveitamento Conceito
Entre 9,0 e 10,0 ----------A
Entre 7,5 e 9,0 -----------B
Entre 6,0 e 7,5 -----------C
Entre 4,0 e 6,0 -----------D
Entre 4,0 e zero ----------E
"""

n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
m = (n1 + n2) / 2

print(f"Sua média de aproveitamento é: {m:.1f}", end=' ')
if 0 <= m <= 4:
    print("E")
elif 4 < m <= 6:
    print("D")
elif 6 < m <= 7.5:
    print("C")
elif 7.5 < m <= 9:
    print("B")
else:
    print("A")
