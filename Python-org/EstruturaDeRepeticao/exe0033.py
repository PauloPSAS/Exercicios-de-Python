"""O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia a um conjunto
indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das
temperaturas(Vou usar números aleatórios e considerar as Temperaturas em Graus Celsius)."""

import random


def saida(lista, m):
    maior, menor = maior_menorT(lista)
    print(f"Foram registrada {len(lista)} Temperaturas em Graus Celsius.")
    print(f"Temperaturas Registradas: ")
    for cont in lista:
        print(f"{cont:.1f} Cº ")
    print()
    print(f"A maior temperatura Registrada foi de {maior:.1f} Cº.")
    print(f"A menor temperatura registrada foi de {menor:.1f} Cº.")
    print(f"Média das Temperaturas: {m:.1f} Cº.")


def maior_menorT(lista):
    ma = max(lista)
    me = min(lista)
    return ma, me


def temperaturas(qtd):
    lista = list()
    for t in range(1, qtd+1):
        lista.append(round(random.uniform(-10, 45), 1))
    return lista


def media(lista):
    m = 0
    for temp in lista:
        m += temp
    m /= len(lista)
    return m


qtdTemperaturas = int(random.randint(3, 20))
li = temperaturas(qtdTemperaturas)
maior_menorT(li)
me = media(li)
saida(li, me)
