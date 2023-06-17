"""Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
a) Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
b) Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
c) A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. 
Faça um programa que determine o salário atual desse funcionário. 
Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário."""


def exibe_print(s95, p, s):
    print(f"\nSalário do funcionário em 1995 é de: R$ {s95:.2f}\n")
    print(f"Em 1996 ganhou um aumento de {p:.1f} % do salário e passou a ser de: R$ {s:.2f}")
    print("Nos anos subsequentes o percentual de aumento foi dobrando até o ano de 2010.\n")


def anos(s, p, a):
    for ano in range(1997, 2011):

        # Diminui o percentual de aumento e coloquei um range fixo de anos para se parecer mais realista.
        p *= 1.3
        a = s / 100 * p
        s += a
        print(f"No ano de {ano} o aumento foi de {p:.1f}% e o salário passou a ser R$ {s:.2f}.")

# main
salario95 = float(input("Digite o salário do funcionário em 1995: R$ "))
pct = 1.5
aumento = (salario95 / 100) * pct
salario = salario95 + aumento

exibe_print(salario95, pct, salario)
anos(salario, pct, aumento)
print()
