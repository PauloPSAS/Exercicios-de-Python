"""Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                     Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um
desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade
(em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente."""

morangosKg = float(input("Digite quantos Kilos de morango foi comprado: (Kg) "))
macasKg = float(input("Digite quantos Kilos de maças foi comprado: (Kg) "))
print("==" * 30)

morangosValor = macasValor = 0

if morangosKg <= 5:
    morangosValor = 2.50 * morangosKg
else:
    print("Acima de 5.0Kg Morangos custam R$ 2,20.")
    morangosValor = 2.20 * morangosKg

if macasKg <= 5:
    macasValor = 1.80 * macasKg
else:
    print("Acima de 5.0Kg Maçãs custam R$ 1,50.")
    macasValor = 1.50 * macasKg

valorT = morangosValor + macasValor
kgTotal = morangosKg + macasKg

if kgTotal > 8 or valorT > 25:
    print("Compras acima de 8Kg ou maiores que R$ 25,00 ganham mais 10% de desconto.")
    dsc = valorT / 100 * 10
    valorT -= dsc


print("==" * 30)
print(f"Quantidade de morangos é: {morangosKg:.1f}Kg. Custa R$ {morangosValor:.2f}.")
print(f"Quantidade de maçãs é: {macasKg:.1f}Kg. Custa R$ {macasValor:.2f}.")
print(f"Quantidade total é de: {kgTotal:.1f}Kg. Custa R$ {valorT:.2f}.")
