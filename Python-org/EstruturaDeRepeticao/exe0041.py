"""Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados:
valor da dívida,
valor dos juros,
quantidade de parcelas e valor da parcela.

Quantidade de Parcelas % de Juros sobre o valor inicial da dívida
    1       0
    3       10
    6       15
    9       20
    12      25"""

divida = float(input("Digite o valor da divida: R$ "))
while True:
    parcelas = int(input("\nDigite em quantas parcelas será dividido a divida (entre 1 e 12): "))
    if parcelas <= 0 or parcelas > 12:
        print("\nDigite um valor de parcelas válidos entre 1 e 12.")
    else:
        break
if parcelas > 9:
    pct = 25
elif parcelas > 6:
    pct = 20
elif parcelas > 3:
    pct = 15
elif parcelas > 1:
    pct = 10
else:
    pct = 0

valorJuros = divida / 100 * pct
dividaFinal = divida + valorJuros
valorParcelas = dividaFinal / parcelas

print(f"\nValor da dívida: R$ {divida:.2f}")
print(f"Valor de {pct}% de juros sobre as {parcelas} parcela(s): R$ {valorJuros:.2f}")
print(f"Valor final é de R$ {dividaFinal:.2f} divido em {parcelas} parcelas de R$ {valorParcelas:.2f}.")
