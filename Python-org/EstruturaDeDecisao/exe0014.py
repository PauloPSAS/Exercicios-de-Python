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
s = ''
c = ''

if 0 <= m <= 4:
    c = 'REPROVADO'
    s = 'E'
elif 4 < m <= 6:
    c = 'REPROVADO'
    s = 'D'
elif 6 < m <= 7.5:
    c = 'APROVADO'
    s = 'C'
elif 7.5 < m <= 9:
    c = 'APROVADO'
    s = 'B'
else:
    c = 'APROVADO'
    s = 'A'

print("{:<23} {:>9}".format("Média de Aproveitamento", "Conceito"))
print("{:>7.1f} {:>9} {:>16}".format(m, s, c))
