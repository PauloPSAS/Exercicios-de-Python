"""A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a
 série até o n−ésimo termo."""


def fibonacci(n):
    n1 = total = 0
    n2 = 1
    c = 3
    print(f"{n2}", end='')
    while c <= n:
        n3 = n1 + n2
        total = n2 + n3
        print(f' -> {n3}', end='')
        n1 = n2
        n2 = n3
        c += 1
    print(f" = {total}")


num = int(input("Digite o número para o tamanho da sequência de Fibonacci: "))
fibonacci(num)
