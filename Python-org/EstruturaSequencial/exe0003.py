# Faça um Programa que peça dois números e imprima a soma.
def msg_erro():
    print("\n\033[1;31mDigite um número inteiro.\033[m\n")


def soma(v1, v2):
    return v1 + v2


while True:
    while True:
        a = input("Digite um número: ")
        if a.isnumeric():
            break
        else:
            msg_erro()
    while True:
        b = input("Digite outro número: ")
        if b.isnumeric():
            break
        else:
            msg_erro()
    break
print(f"\nA soma de {int(a)} + {int(b)} é igual à {soma(int(a), int(b))}")
