"""Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
    até 20 litros, desconto de 3% por litro
    acima de 20 litros, desconto de 5% por litro
Gasolina:
    até 20 litros, desconto de 4% por litro
    acima de 20 litros, desconto de 6% por litro
Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma:
A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro
da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90."""

print("""
GASOLINA R$ 2,50 l
ÁLCOOL R$ 1,90 l
Álcool:
    até 20 litros, desconto de 3% por litro
    acima de 20 litros, desconto de 5% por litro
Gasolina:
    até 20 litros, desconto de 4% por litro
    acima de 20 litros, desconto de 6% por litro\n""")

while True:
    combustivel = input("Digite 'A' para álcool ou 'G' para gasolina: ").upper()[0]
    if combustivel != 'A' and combustivel != 'G':
        print("\nDigite apenas A ou G...\n")
    else:
        break

litros = float(input("\nDigite quantos litros foi comprado: (l) "))

valorF = 0
if combustivel == 'A':
    if litros <= 20:
        print("Vai ganhar 3% de desconto.")
        valor = 1.90 * litros
        dsc = valor / 100 * 3
        valorF = valor - dsc
    else:
        print("Vai ganhar 5% de desconto.")
        valor = 1.90 * litros
        dsc = valor / 100 * 5
        valorF = valor - dsc

elif combustivel == 'G':
    if litros <= 20:
        print("Vai ganhar 4% de desconto.")
        valor = 2.50 * litros
        dsc = valor / 100 * 4
        valorF = valor - dsc
    else:
        print("Vai ganhar 6% de desconto.")
        valor = 2.50 * litros
        dsc = valor / 100 * 6
        valorF = valor - dsc
print(f"O cliente irá pagar R$ {valorF:.2f} nos {litros}l de combustivel.")
