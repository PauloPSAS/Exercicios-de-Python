# Faça um Programa que converta metros para centímetros.
def centimetros(metros):
    return metros * 100


m = float(input("Digite quantos metros deseja converter: "))
print("{:.1f}m equivale a {:.1f}cm".format(m, centimetros(m)))
