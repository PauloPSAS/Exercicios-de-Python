"""Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
 a) o produto do dobro do primeiro com metade do segundo.
 b) a soma do triplo do primeiro com o terceiro.
 c) o terceiro elevado ao cubo."""


def a(xx, yy):
    return (xx * 2) * (yy / 2)


def b(xx, zz):
    return (xx * 3) + zz


def c(zz):
    return zz ** 3


x = int(input("Digite um número inteiro: "))
y = int(input("Digite outro número inteiro: "))
z = float(input("Agora digite um número real: "))

# Função correspondente à resposta da letra 'a' no comentário inicial.
print("\nO Produto do dobro de {} com a metade de {} é: {}.".format(x, y, a(x, y)))

# Funçao coprrespondente a resposta da letra 'b' no comentário inicial.
print("A soma do triplo de {} com {} é: {:.1f}.".format(x, z, b(x, z)))

# Função correspondente à resposta da letra'c' no comentário inicial
print("{:.1f} elevado ao cubo é: {:.1f}".format(z, c(z)))
