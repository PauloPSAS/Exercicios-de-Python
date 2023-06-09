"""Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O
programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão
avaliados o funcionamento, o estilo e o número de testes (divisões) executados."""


def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True


def primos_ate_n(n):
    primos = list()
    divisoes = 0
    for i in range(2, n + 1):
        if eh_primo(i):
            primos.append(i)
            divisoes += 1
    return primos, divisoes


num = int(input("Digite um número inteiro: "))
nPrimos, nDivisoes = primos_ate_n(num)

print(f"Números primos entre 1 e {num}: ", end='')
for primo in nPrimos:
    print(primo, end=' ')
print()

print("número de divisões executadas: {}".format(nDivisoes))
