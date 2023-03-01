"""João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu
trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São
Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que
leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do
limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens
adequadas."""


def excesso(kg):
    ex = peso - 50.0
    multa = ex * 4.0
    return ex, multa


peso = float(input("Quantos kilos João papo-de-Pescador trouxe? Kg "))
execido, mult = excesso(peso)
if peso <= 50:
    print(f"João papo-de-pescador trouxe {peso}Kg. Não excedeu o limite estabelecido pelo regulamento.")
else:
    print(f"João papo-de-pescador trouxe {peso}Kg. ele excedeu {execido:.1f}Kg, vai ganhar R$ {mult:.2f} de multa.")
