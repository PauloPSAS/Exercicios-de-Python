"""Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos
existentes entre 1 e um número inteiro informado pelo usuário."""


def exibe_num_primo(num):
    contador1 = 1
    while contador1 <= num:
        divisoes = 0
        contador2 = 1
        while contador2 <= contador1:
            if contador1 % contador2 == 0:
                divisoes += 1
            contador2 += 1
        if divisoes == 2:
            print(contador1, end=' ')
        contador1 += 1


numero = int(input("Digite um número inteiro: "))
exibe_num_primo(numero)
