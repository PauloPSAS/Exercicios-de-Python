def gerador_de_num_int(ma, me):
    for n in range(me, ma + 1):
        if n != ma:
            print(n, end=' - ')
        else:
            print(n)


def entrada():
    n1 = int(input("Digite um número inteiro qualquer: "))
    n2 = int(input("Digite outro número inteiro qualquer: "))
    return n1, n2


def separador():
    while True:
        v1, v2 = entrada()

        if v1 > v2:
            maior = v1
            menor = v2
            break
        elif v2 > v1:
            maior = v2
            menor = v1
            break
        else:
            print("Os valores devem ser diferentes.")
    return menor, maior


menor, maior = separador()

print(f"\nNúmeros inteiros do intervalo entre {menor} e {maior}.")
gerador_de_num_int(maior, menor)
