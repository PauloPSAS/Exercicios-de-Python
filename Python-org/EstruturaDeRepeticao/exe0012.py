"""Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve
informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
Tabuada de 5:
    5 X 1 = 5
    5 X 2 = 10
    ...
    5 X 10 = 50
"""


def tabuada(v):
    for i in range(1, 11):
        print(f"{v} x {i} = {v * i}")


n = int(input("Digite um número inteiro: "))
print("==" * 25)
print(f'TABUADA DO {n}.')
print("==" * 25)
tabuada(n)
print("==" * 25)