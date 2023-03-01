"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre
o total do seu salário no referido mês."""


def salario(h, t):
    return h * t


sHora = float(input("Digite o quanto você ganha por hora: R$ "))
hTrabalho = float(input("Digite quantas horas trabalhadas no mês: "))
total = salario(sHora, hTrabalho)
print(f"Você ganha R$ {sHora:.2f} por hora e trabalhou {hTrabalho} horas esse mês. Seu salário será R$ {total:.2f}")
