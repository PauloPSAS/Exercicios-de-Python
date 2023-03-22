"""Faça um programa que leia e valide as seguintes informações:
a) Nome: maior que 3 caracteres;
b) Idade: entre 0 e 150;
c) Salário: maior que zero;
d) Sexo: 'f' ou 'm';
e) Estado Civil: 's', 'c', 'v', 'd';"""

nome = input("Nome: ")
while len(nome) <= 3:
    print("\nDigite um nome maior que 3 caracteres.")
    nome = input("Nome: ")
print("Nome Validado.\n")

idade = int(input("Idade: "))
while idade < 0 or idade > 150:
    print("\nDigite a idade entre 0 e 150 anos.")
    idade = int(input("Idade: "))
print("Idade validada.\n")

salario = float(input("Salário: R$ "))
while salario <= 0:
    print("\nDigite o salário acima de R$ 0,0.")
    salario = float(input("Salário: R$ "))
print("Salário validado.\n")

sexo = str(input("Sexo: [M/F] ")).upper()
while True:
    if sexo == 'M' or sexo == 'F':
        break
    else:
        print("\nDigite apenas M ou F para os respectivos sexos.")
        sexo = str(input("Sexo: [M/F] ")).upper()
print("Sexo Validado.\n")

ec = {'s': 'Solteiro(a)', 'c': 'Casado(a)', 'v': 'Viúvo(a)', 'd': 'Divorciado(a)'}

estadoCivil = str(input("Estado civil: [s(solteiro(a)) / c(casado(a)) / v(viúvo(a)) / d(divorciado(a))] ")).lower()
while estadoCivil not in ec:
    print("\nDigite apenas uma das respectivas opções [s/c/v/d].")
    estadoCivil = str(input("Estado civil: [s(solteiro(a)) / c(casado(a)) / v(viúvo(a)) / d(divorciado(a))] ")).lower()
print("Estado Civil Validado.\n")

print("==" * 20)
print(f"Nome é: {nome}.")
print(f"Idade é: {idade} anos.")
print(f"Salário é: R$ {salario:.2f}.")
print(f"Sexo é: {sexo}.")
print(f"Estado Civil é: {ec[estadoCivil]}")
print("==" * 20)
