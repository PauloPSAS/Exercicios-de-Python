"""Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
'Telefonou para a vítima?'
'Esteve no local do crime?'
'Mora perto da vítima?'
'Devia para a vítima?'
'Já trabalhou com a vítima?'
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como 'Suspeita',
entre 3 e 4 como 'Cúmplice' e 5 como 'Assassino'. Caso contrário, ele será classificado como 'Inocente'."""


def msg_erro():
    print("\nDigite apenas S para Sim ou N para Não.\n")


print("""Estamos fazendo uma investigação para descobrir o assasino de um crime que aconteceu com alguém que você 
conhece. Por favor colabore e responda as perguntas apenas com 'S' ou 'N'.""")
pos = neg = 0
while True:
    q = str(input("Você ja telefonou para a vítima? [S/N] ")).upper()

    if q == 'S':
        pos += 1
        break
    elif q == 'N':
        neg += 1
        break

    if q != 'S' and q != 'N':
        msg_erro()

print()
while True:
    q = input("Você esteve no local do crime? [S/N] ").upper()

    if q == 'S':
        pos += 1
        break
    elif q == 'N':
        neg += 1
        break

    if q != 'S' and q != 'N':
        msg_erro()

print()
while True:
    q = input("Você mora perto da vítima?  [S/N] ").upper()

    if q == 'S':
        pos += 1
        break
    elif q == 'N':
        neg += 1
        break

    if q != 'S' and q != 'N':
        msg_erro()

print()
while True:
    q = input("Você devia para a vítima?  [S/N] ").upper()

    if q == 'S':
        pos += 1
        break
    elif q == 'N':
        neg += 1
        break

    if q != 'S' and q != 'N':
        msg_erro()

print()
while True:
    q = input("Você já trabalhou com a vítima?  [S/N] ").upper()

    if q == 'S':
        pos += 1
        break
    elif q == 'N':
        neg += 1
        break

    if q != 'S' and q != 'N':
        msg_erro()

print("\n")
print("==" * 20)
if pos <= 1:
    print("Você é INOCENTE.")
elif pos <= 2:
    print("Você é SUSPETO(A).")
elif pos <= 4:
    print("Você é CUMPLICE.")
elif pos == 5:
    print("Você é o ASSASINO.")
print("==" * 20)
