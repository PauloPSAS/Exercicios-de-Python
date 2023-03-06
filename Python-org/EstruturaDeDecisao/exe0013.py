"""Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
se digitar outro valor deve aparecer valor inválido."""

dias = ['Domingo', 'Segunda-Feira', 'Terça-Feira', 'Quarta-Feira', 'Quinta-Feira', 'Sexta-Feira', 'Sábado']

while True:
    num = int(input("Digite um número de 1 a 7: "))
    if num > 7 or num < 1:
        print("\033[31mvalor inválido!\033[m")
        print("\033[32mDigite apenas um número inteiro entre 1 e 7.\033[m\n")
    else:
        break

print("\033[1;33m")
print(dias[num-1])
