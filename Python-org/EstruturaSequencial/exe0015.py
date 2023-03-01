"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre
o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e
5% para o sindicato, faça um programa que nos dê:
a) salário bruto.
b) quanto pagou ao INSS.
c) quanto pagou ao sindicato.
d) o salário líquido.

Calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
"""


def saida(salario_hora, horas_trabalhadas):
    salarioBruto = salario_hora * horas_trabalhadas
    ir = salarioBruto / 100 * 11
    inss = salarioBruto / 100 * 8
    sindicato = salarioBruto / 100 * 5
    salarioLiquido = salarioBruto - (ir + inss + sindicato)

    print(f"\033[33mSalário Bruto :  R$ {salarioBruto:.2f}.")
    print(f"\033[31mIR (11%) : R$ {ir:.2f}.")
    print(f"INSS (8%) : R$ {inss:.2f}.")
    print(f"Sindicato (5%) : R$ {sindicato:.2f}.")
    print(f"\033[36mSalário Liquido : R$ {salarioLiquido:.2f}")


salarioHoras = float(input("Digite seu salário por horas: R$ "))
horasTrabalhadas = float(input("Digite quantas horas trabalhadas: "))

saida(salarioHoras, horasTrabalhadas)
