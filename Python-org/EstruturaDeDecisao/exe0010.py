"""Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N-
Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso."""

turn = str(input("Em que turno você estuda? [M(Manhã)/T(Tarde)/N(Noite)] ")).upper()
print("\n")
if turn == 'M':
    print("Bom Dia!")
elif turn == 'T':
    print("Boa Tarde!")
elif turn == 'N':
    print("Boa Noite!")
else:
    print("Valor Inválido...")
