"""Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada
eleitor votar e ao final mostrar o número de votos de cada candidato. Optei por deixar os números aleatórios
escolherem os candidatos mais votados."""
import time


def ganhou(a, b, c):
    name = 'A(15)'
    maior = a
    if b > maior and b > c:
        name = 'B(10)'
        maior = b
    elif c > maior and c > b:
        name = 'C(23)'
        maior = c
    return maior, name


def votacao(cdt, elt):
    import random

    a = b = c = t = 0
    for v in range(1, elt + 1):
        voto = random.choice(candidaos)
        if voto == cdt[0]:
            a += 1
        elif voto == cdt[1]:
            b += 1
        else:
            c += 1
        t += 1
    return a, b, c, t


candidaos = [15, 10, 23]

eleitores = int(input("Digite quantos eleitores têm para votar: "))
time.sleep(1)

print("Há três cadidatos o candidato A(15), B(10) e C(23).")
print("Eleitores estão votando, aguarde...")
cdtA, cdtB, cdtC, total = votacao(candidaos, eleitores)
time.sleep(5)

print(f"Todos os {total} votos foram feitos.")
time.sleep(.6)

print(f"O resultado da eleição aleatória é:\n\nCandidato A(15) teve {cdtA} votos.")
time.sleep(1)

print(f"O Canditado B(10) teve {cdtB} votos.")
time.sleep(1)

print(f"O candidato C(23) teve {cdtC} votos.")
time.sleep(1.5)

vencedor, nome = ganhou(cdtA, cdtB, cdtC)
print(f"O CAMPEÃO É O CANDIDATO '{nome}' COM {vencedor} VOTOS!\n")
