"""Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário,
mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser
informados também pelo usuário, conforme exemplo abaixo:

    Montar a tabuada de: 5
    Começar por: 4
    Terminar em: 7

    Vou montar a tabuada de 5 começando em 4 e terminando em 7:
    5 X 4 = 20
    5 X 5 = 25
    5 X 6 = 30
    5 X 7 = 35"""


def exibe_tabuada(tab, com, ter):
    print(f"\nVou montar a tabuada de {tab} começando em {com} e terminando em {ter}:")
    for v in range(com, ter + 1):
        print("{} X {} = {}".format(tab, v, tab * v))


tabuada = int(input("Montar a tabuada de: "))
comeca = int(input("começar por: "))
while True:
    termina = int(input("Terminar em: "))
    if termina <= comeca:
        print("\nDigite um valor maior do que o começo para terminar a tabuada...")
    else:
        break
exibe_tabuada(tabuada, comeca, termina)
