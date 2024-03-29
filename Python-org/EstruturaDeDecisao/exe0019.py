"""Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades
do mesmo.
    Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
    326 = 3 centenas, 2 dezenas e 6 unidades
    12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e
    16"""

print("Digite um número maior ou igual à 0 e menor que 1000: ", end='')
numero = int(input())
if numero < 0 or numero >= 1000:
    print("Valor inválido.")

unidade = numero % 10
numero = (numero - unidade) / 10

dezena = numero % 10
numero = (numero - dezena) / 10

centena = numero

dezena = int(dezena)
centena = int(centena)

if centena > 0:
    print(f"{centena} centena(s), {dezena} dezena(s) e {unidade} unidade(s).")
elif centena == 0 and dezena > 0:
    print(f"{dezena} dezena(s) e {unidade} unidade(s).")
else:
    print(f"{unidade} unidade(s).")
