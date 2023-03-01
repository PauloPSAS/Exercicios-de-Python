"""Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando
as seguintes fórmulas: Para homens: (72.7*h) - 58. Para mulheres: (62.1*h) - 44.7 """


def peso_ideal(alt, s):
    if s == "M":
        return (72.7 * alt) - 58
    else:
        return (62.1 * alt) - 44.7


altura = float(input("Informe sua altura: "))
while True:
    sexo = str(input("Informe seu sexo: [F/M] ")).upper()
    if sexo == "F" or sexo == "M":
        break
    else:
        print("\nInforme apenas 'M' para masculino ou 'F' para feminino.")
pesoIdeal = peso_ideal(altura, sexo)
print(f"O peso ideal para você é: {pesoIdeal:.2f}")
