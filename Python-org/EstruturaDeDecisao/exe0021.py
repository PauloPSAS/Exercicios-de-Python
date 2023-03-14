"""Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois
informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 20, 50 e 100 reais.
O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas
existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece 2 notas de 100, 1 nota de 50,
1 nota de 5 e 1 nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100,
uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1."""

print("Valor minímo para saque é de 10 reais e o valor máximo é de 600 reais")
saque = int(input("Quanto vai sacar? R$ "))

while (saque < 10) or (saque > 600):
    print("\nValor do saque está fora dos limites permitido.\n")
    saque = int(input("Digite novamente: R$ "))

total = saque
ced = 100
tCed = 0

while True:
    if total >= ced:
        total -= ced
        tCed += 1
    else:
        if tCed > 0:
            print(f"Total de {tCed} cédula(s) de R$ {ced}")
        if total < 5:
            ced = 1
        elif total < 10:
            ced = 5
        elif total < 20:
            ced = 10
        elif total < 50:
            ced = 20
        elif total < 100:
            ced = 50
        tCed = 0
        if total == 0:
            break

