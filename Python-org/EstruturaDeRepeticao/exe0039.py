"""Faça um programa que leia dez conjuntos de dois valores,
o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros.
Encontre o aluno mais alto e o mais baixo.
Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas."""
def lista_alunos():
        num = int(input("Digite o número do aluno(a): "))
        alt = float(input("Digite a altura do aluno(a): m "))
        print()
        return num, alt


def maior():

    for i in range(1, 11):
        numero, altura = lista_alunos()
        if i == 1:
            alto = altura
            numeAlt = numero
            baixo = altura
            numeBxo = numero
        else:
            if altura > alto:
                alto = altura
                numeAlt = numero
            if altura < baixo:
                 baixo = altura
                 numeBxo = numero
    return alto, numeAlt, baixo, numeBxo


maisAlto, numeroA, maisBaixo, numeroB = maior()
print("\nNúmero do aluno mais alto: {}. Altura é m {:.2f}".format(numeroA, maisAlto))
print("Número do aluno mais baixo: {}. Altura é m {:.2f}".format(numeroB, maisBaixo))
