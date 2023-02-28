"""Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e em que
a soma das linhas, colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:
8  3  4
1  5  9
6  7  2
Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as
características acima. Dica: produza todas as combinações possíveis e verifique a soma quando completar cada
quadrado. Usar um vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3."""


def gera_combinacoes(lista, n):
    #  gera tupla com todas as combinações possíveis da soma de três números da lista
    #  que seja iguais a 15.
    for i in lista:
        for j in lista:
            if n + i + j == 15 and (n != i and n != j and i != j):
                combinacoes.append((n, i, j))


def gera_quadro(comb, L1):
    linha1 = L1
    for i in range(len(comb)):
        linha2 = comb[i]
        for j in range(len(comb)):
            linha3 = comb[j]

            if (linha1[0] + linha2[0] + linha3[0] == 15) and \
                    (linha1[1] + linha2[1] + linha3[1] == 15) and \
                    (linha1[2] + linha2[2] + linha3[2] == 15) and \
                    (linha1[0] + linha2[1] + linha3[2] == 15) and \
                    (linha1[2] + linha2[1] + linha3[0] == 15):

                if (linha1[0] not in linha2) and \
                        (linha1[1] not in linha2) and \
                        (linha1[2] not in linha2):
                    print(linha1)
                    print(linha2)
                    print(linha3)
                    print()


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
combinacoes = []

for n in range(1, 10):
    gera_combinacoes(lista, n)

print()

for L1 in combinacoes:
    gera_quadro(combinacoes, L1)
