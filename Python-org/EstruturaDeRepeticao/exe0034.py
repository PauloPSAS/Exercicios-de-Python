"""Os números primos possuem várias aplicações na Computação, por exemplo, na Criptografia. Um número primo é
aquele sendo divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se
ele é ou não um número primo."""


def primo(num):
    total = 0
    for c in range(1, num+1):
        if num % c == 0:
            total += 1
    if total == 2:
        print("\033[34m{} é um NÚMERO PRIMO.".format(num))
    else:
        print("\033[31m{} não é um NÚMERO PRIMO.".format(num))


numero = int(input("Digite um número inteiro: "))
primo(numero)