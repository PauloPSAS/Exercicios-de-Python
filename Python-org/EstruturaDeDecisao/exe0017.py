"""Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não
bissexto."""
import datetime as dt
red = '\033[31m'
blue = '\033[34m'
while True:
    ano = int(input("Digite um ano (ex: 1945) ou digite 0 para o ano atual: "))
    if ano == 0:
        ano = dt.date.today().year
        break
    if 1000 <= ano <= 9999:
        break
    else:
        print("Digite apenas um ano com 4 digitos...\n")


if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"{blue}O ano {ano} é BISSEXTO.")
else:
    print(f"{red}O ano {ano} NÃO é BISSEXTO")
