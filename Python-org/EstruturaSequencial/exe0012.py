"""Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
usando a seguinte fórmula: (72.7*altura) - 58"""


def peso_ideal(alt):
    return (72.7 * alt) - 58


altura = float(input("Digite sua altura: m "))

print(f"O peso ideal para {altura}m é: {peso_ideal(altura):.2f}")
