"""Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O
resultado da operação deve ser acompanhado de uma frase que diga se o número é:
a) par ou ímpar;
b) positivo ou negativo;
c) inteiro ou decimal."""

n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
print("Qual operação você deseja relizar? ")
print("==" * 20)
print("""
         1 - para adição
         2 - para subtração
         3 - para multiplicação
         4 - para divisão
""")
print("==" * 20)
while True:
    rsp = int(input("Escolha a operação matemática: "))
    if rsp < 1 or rsp > 4:
        print("\nEscolha apenas uma das 4 escolhas fornecidas.\n")
    else:
        break
t = 0
if rsp == 1:
    t = n1 + n2
    if t == round(t):
        print(f"{n1:.0f} + {n2:.0f} = {t:.0f}")
    else:
        print(f"{n1} + {n2} = {t}")
elif rsp == 2:
    t = n1 - n2
    if t == round(t):
        print(f"{n1:.0f} - {n2:.0f} = {t:.0f}")
    else:
        print(f"{n1} - {n2} = {t}")
elif rsp == 3:
    t = n1 * n2
    if t == round(t):
        print(f"{n1:.0f} * {n2:.0f} = {t:.0f}")
    else:
        print(f"{n1} * {n2} = {t}")
elif rsp == 4:
    t = n1 / n2
    if t == round(t):
        print(f"{n1:.0f} / {n2:.0f} = {t}")
    else:
        print(f"{n1} / {n2} = {t}")

print("\n")
if t % 2 == 0:
    print(f"{t} é um número PAR.")
elif t % 2 != 0:
    print(f"{t} é um número ÍMPAR.")
elif t == 0:
    print(f"{t} é um número NEUTRO.")

if t > 0:
    print(f"{t} é POSITIVO.")
elif t < 0:
    print(f"{t} é NEGATIVO.")
else:
    print(f"{t} é um númeor NEUTRO.")

if t == round(t):
    print(f"{t} é um número inteiro.")
else:
    print(f"{t} é um número décimal.")
