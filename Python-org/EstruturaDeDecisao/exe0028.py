"""O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                           até 5Kg            Acima de 5Kg
    File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
    Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
    Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

    Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente
receberá ainda um desconto de 5% sobre o total da compra.
Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal,
contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento,
valor do desconto e valor a pagar."""

print("--" * 20)
print(f"\033[1;35m{'Hipermercado Tabajara':^40}\033[m")
print("--" * 20)
print("\033[32mTipos de carnes disponíveis:")
print("""\033[3;32m( 1 ) - File Duplo R$ 4,90. Acima de 5Kg é R$ 5,80.
( 2 ) - Alcatra R$ 5,90. Acima de 5Kg é 6,80.
( 3 ) - Picanha R$ 6,90. Acima de 5Kg é 7,80.\033[m\n""")

carne = valor = desconto = valorF = vk = 0
tipoCarne = ''

while True:
    carne = int(input("Digite o número correspondente ao tipo de carne escolhida: "))
    if 1 <= carne <= 3:
        break
    else:
        print("\n\033[3;32mEscolha apenas umas das carnes corrspondentes no menu.\n")
        print("""
        ( 1 ) - File Duplo R$ 4,90. Acima de 5Kg é R$ 5,80.
        ( 2 ) - Alcatra R$ 5,90. Acima de 5Kg é 6,80.
        ( 3 ) - Picanha R$ 6,90. Acima de 5Kg é 7,80.\033[m\n""")
kg = float(input("Quantos Kilos será? (Kg) "))
print("\n\033[1mPagamentos feitos com o cartão Tabajara terá mais 5% de desconto.\033[m\n")
while True:
    tc = str(input("A compra será paga com o cartão Tabajara? [S/N] ")).upper()
    if tc == 'S' or tc == 'N':
        break
    else:
        print("\033[31mEscolha apenas 'S' para SIM ou 'N' para NÃO.\033[m")

# File Duplo
if carne == 1:
    tipoCarne = 'File Duplo'
    if kg <= 5:
        vk = 4.90
        valor = vk * kg
    else:
        vk = 5.80
        valor = vk * kg

# Alcatra
elif carne == 2:
    tipoCarne = 'Alcatra'
    if kg <= 5:
        vk = 5.90
        valor = vk * kg
    else:
        vk = 6.80
        valor = vk * kg

# Picanha
elif carne == 3:
    tipoCarne = 'Picanha'
    if kg <= 5:
        vk = 6.90
        valor = vk * kg
    else:
        vk = 7.80
        valor = vk * kg

if tc == 'S':
    desconto = valor / 100 * 5
    valorF = valor - desconto
else:
    valorF = valor

print("--" * 25)
print("\033[3;35m{:^50}\033[m".format('Cupom Fiscal'))
print("--" * 25)
print("\033[1;33m")
print(f"{'Tipo de Carne':<34} : {tipoCarne}")
print(f"{'Quantidade':<34} : {'Kg'} {kg:.1f}")
print(f"{'Valor do Kilo':<34} : {'R$'} {vk:.2f}")
print(f"{'pagamento com cartão Tabajara':<34} : {tc}")
if tc == 'S':
    print(f"{'Desconto de 5 % do cartão Tabajara':<34} : {'R$'} {desconto:>5.2f}")
print(f"{'valor Total':<34} : {'R$'} {valorF:.2f}")
print("\033[m" + ("==" * 25))
