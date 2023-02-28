"""Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função
deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor
máximo é 20. Se valores fora da faixa forem informados, eles devem ser modificados para valores na faixa de
forma elegante."""


def msg_erro():
    print("\nDigite um número inteiro entre 1 e 20...\n")


def entrada():
    while True:
        while True:
            larg = int(input("Digite a largura entre 1 e 20: "))
            if 1 <= larg <= 20:
                break
            else:
                msg_erro()

        while True:
            alt = int(input("Digite a altura entre 1 e 20: "))
            if 1 <= alt <= 20:
                break
            else:
                msg_erro()
        break
    return larg, alt


def saida(larg, alt):
    # borda superior
    print("+" * larg)

    # bordas laterais
    for a in range(alt - 2):
        print("|" + " " * (larg - 2) + "|")

    # borda inferior
    print("-" * larg)


al, la = entrada()
saida(al, la)
