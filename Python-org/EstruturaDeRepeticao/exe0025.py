"""Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da
turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média
calculada."""


def media_idade(qtd, idds):
    media = 0
    for idade in idds:
        media += idade
    media /= qtd
    return media


def idades(qtd):
    idadesTurma = []
    for pessoa in range(1, qtd + 1):
        idadesTurma.append(int(input(f"Digite a idade da {pessoa}ª pessoa: ")))
    return idadesTurma


def saida(m):
    if m >= 60:
        return 'idosa'
    elif m >= 28:
        return 'adulta'
    elif m >= 18:
        return 'jovem'
    else:
        return 'adolescente'


qtdPessoas = int(input("Quantas pessoas têm na turma: "))
idadesLista = idades(qtdPessoas)
mIdade = media_idade(qtdPessoas, idadesLista)
print(f"\nNa turma têm {qtdPessoas} alunos, a média da idade da turma é de {mIdade:.1f}, uma turma {saida(mIdade)}.")
