"""Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por
aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez."""

n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
m = (n1 + n2) / 2
print("\nMédia é: {:.1f}".format(m))
if m > 7:
    print("Aluno APROVADO.")
elif m < 7:
    print("Aluno REPROVADO.")
else:
    print("Aprovado com DISTINÇÃO.")
