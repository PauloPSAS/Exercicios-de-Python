"""Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide
a entrada e permita repetir a operação."""

a = int(input("Digite o números de habitantes que terá o estado 'A': "))
print("\nO número de habitantes do estado 'B' tem que ser maior que o estado 'A' para o cálculo "
      "funcionar corretamente.\n")
b = int(input("Digite o número de habitantes que terá o estado 'B': "))
while a >= b:
    print("\ntente digitar uma quantidade de habitantes maior para o estado 'B'.\n")
    b = int(input("Digite o número de habitantes que terá o estado 'B': "))
print("\n")
ca = float(input("Taxa de crescimento anual do estado 'A' em %: "))
cb = float(input("Taxa de crescimento anual do estado 'B' em %: "))
while cb >= ca:
    print("\nDigite um crescimento anual maior para o estado 'A'.\n")
    ca = float(input("Taxa de crescimento anual do estado 'A' em %: "))
c = 0
while a <= b:
    a = a + (a / 100 * ca)
    b = b + (b / 100 * cb)
    c += 1

print(f"'A' ultrapassará 'B' em {c} anos.")
print(f"'A' terá população de {a:.1f} habitantes e 'B' terá {b:.1f} habitantes.")
