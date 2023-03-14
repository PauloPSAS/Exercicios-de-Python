"""Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por
aluno e presentar:
a) A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
b) A mensagem "Reprovado", se a média for menor que 7, com a respectiva média alcançada;
c) A mensagem "Aprovado com Distinção", se a média for igual a 10."""

cond = ''
n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
n3 = float(input("Terceira nota: "))

m = (n1 + n2 + n3) / 3

if m == 10:
    cond = '\033[34mAPROVADO com Distinção\033[m'
elif m >= 7:
    cond = '\033[33mAPROVADO\033[m'
else:
    cond = '\033[31mREPROVADO\033[m'

print(f"{cond}. Sua nota foi {m:.1f}.")
