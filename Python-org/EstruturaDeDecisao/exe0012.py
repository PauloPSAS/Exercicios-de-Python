"""Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário
Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os
descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20%
Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade
de hora é 220."""

hT = float(input("Digite quantas horas foram trabalhadas: (H) "))
sH = float(input("Digite quanto você ganha por hora: R$ "))

sB = hT * sH
inss = sB / 100 * 10
fgts = sB / 100 * 11

if sB <= 900:
    pD = 0
    ir = 0

elif sB <= 1500:
    pD = 5
    ir = sB / 100 * pD

elif sB <= 2500:
    pD = 10
    ir = sB / 100 * pD

else:
    pD = 20
    ir = sB / 100 * pD

tD = ir + inss
sL = sB - tD

print("\033[35m==" * 25)
print(f"\033[1;33m{'Salário Bruto ':<25} : {'R$'} {sB:>10.2f}")
print(f"\033[1;31m{f'(-) IR ({pD}%)':<25} : {'R$'} {ir:>10.2f}")
print(f"\033[1;31m{'(-) INSS ( 10 % )':<25} : {'R$'} {inss:>10.2f}")
print(f"\033[1;32m{'FGTS (11%)':<25} : {'R$'} {fgts:>10.2f}")
print(f"\033[1;31m{'Total de descontos':<25} : {'R$'} {tD:>10.2f}")
print(f"\033[1;34m{'Salário Liquido':<25} : {'R$'} {sL:>10.2f}")
print("\033[35m==" * 25)
