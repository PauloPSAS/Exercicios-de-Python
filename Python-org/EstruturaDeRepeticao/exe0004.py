"""Supondo que a população de um país 'A' seja da ordem de 80.000 habitantes com uma taxa anual de crescimento de 3% e
que a população de 'B', seja 200.000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e
escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B,
mantidas as taxas de crescimento."""

a = 80000
b = 200000
c = 0

while a <= b:
    a = a + (a / 100 * 3)
    b = b + (b / 100 * 1.5)
    c += 1

print(f"'A' ultrapassará a população 'B' em {c} anos.")
print(f"'A' terá população de {a:.1f} habitantes e 'B' terá {b:.1f} habitantes.")
