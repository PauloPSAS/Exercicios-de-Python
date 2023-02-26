# Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.
def reverso(value):
    return str(value)[::-1]


while True:
    num = str(input("Digite um número inteiro: "))
    if num.isnumeric():
        break
    else:
        print("\033[31mApenas um número inteiro qualquer (Sem '.' ou ',' ou casas décimais)\033[m.\n")
r = reverso(num)
print(f"O contrário de \033[1;33m{num}\033[m é \033[1;34m{r}\033[m")
