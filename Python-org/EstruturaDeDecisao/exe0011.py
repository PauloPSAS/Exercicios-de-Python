"""As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver
o programa que calculará os reajustes. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o
seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1 500,00 : aumento de 10%
salários de R$ 1 500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento."""

salarioAtual = float(input("Quaé o salário atual do funcionário: R$ "))
salarioFinal = 0
porcAumento = 0
valorAumento = 0

if salarioAtual < 280.00:
    porcAumento = 20
    valorAumento = salarioAtual / 100 * porcAumento
    salarioFinal = salarioAtual + valorAumento
elif 280.00 <= salarioAtual < 700.00:
    porcAumento = 15
    valorAumento = salarioAtual / 100 * porcAumento
    salarioFinal = salarioAtual + valorAumento
elif 700.00 <= salarioAtual < 1500.00:
    porcAumento = 10
    valorAumento = salarioAtual / 100 * porcAumento
    salarioFinal = salarioAtual + valorAumento
else:
    porcAumento = 5
    valorAumento = salarioAtual / 100 * porcAumento
    salarioFinal = salarioAtual + valorAumento
print()
print(f"\033[31mSalário atual do funcionário: R$ {salarioAtual:.2f}.")
print(f"\033[35mAumento de {porcAumento}%.")
print(f"\033[33mRecebe um aumento de R$ {valorAumento:.2f}.")
print(f"\033[34mValor final do funcionário R$ {salarioFinal:.2f}")
