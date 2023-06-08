"""A série de Fibonacci é formada pela sequência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série
até que o valor seja maior que 500."""


def fibonnaci():
    n1 = 0
    n2 = 1
    contador = 3
    print(f"{n2}", end='')
    while contador <= 16:
        n3 = n1 + n2
        print(f" - {n3}", end='')
        n1 = n2
        n2 = n3
        contador += 1


print("Sequência de Fibonnaci até um valor maior que 500:")
fibonnaci()
